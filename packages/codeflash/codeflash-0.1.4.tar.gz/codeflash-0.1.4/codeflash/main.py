import concurrent.futures
import logging
import sys

from codeflash.cli_cmds.cli import CODEFLASH_LOGO, handle_optimize_all_arg_parsing
from codeflash.code_utils.instrument_existing_tests import inject_profiling_into_existing_test

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s", stream=sys.stdout)
from typing import Optional, Tuple, Union

from codeflash.api import cfapi
from codeflash.api.aiservice import optimize_python_code
from codeflash.cli_cmds.cmd_init import init_codeflash
from codeflash.code_utils import env_utils
from codeflash.code_utils.config_consts import (
    MAX_TEST_RUN_ITERATIONS,
    MAX_FUNCTION_TEST_SECONDS,
    INDIVIDUAL_TEST_TIMEOUT,
    N_CANDIDATES,
)
from codeflash.code_utils.git_utils import (
    get_repo_owner_and_name,
    get_github_secrets_page_url,
    get_current_branch,
    git_root_dir,
)
from codeflash.github.PrComment import FileDiffContent, PrComment


import os
import subprocess
from argparse import ArgumentParser, SUPPRESS, Namespace

import libcst as cst

from codeflash.code_utils.time_utils import humanize_runtime
from codeflash.code_utils.code_extractor import get_code
from codeflash.code_utils.code_replacer import replace_function_in_file
from codeflash.code_utils.code_utils import (
    module_name_from_file_path,
    get_all_function_names,
    get_run_tmp_file,
)
from codeflash.code_utils.config_parser import parse_config_file
from codeflash.discovery.discover_unit_tests import discover_unit_tests, TestsInFile
from codeflash.discovery.functions_to_optimize import (
    get_functions_to_optimize_by_file,
    FunctionToOptimize,
)
from codeflash.optimization.function_context import (
    get_constrained_function_context_and_dependent_functions,
)
from codeflash.verification.equivalence import compare_results
from codeflash.verification.parse_test_output import (
    TestType,
    parse_test_results,
)
from codeflash.verification.test_results import TestResults


from codeflash.verification.test_runner import run_tests
from codeflash.verification.verification_utils import (
    get_test_file_path,
    TestConfig,
)
from codeflash.verification.verifier import generate_tests


def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("command", nargs="?", help="The command to run (e.g., 'init')")
    parser.add_argument("--file", help="Try to optimize only this file")
    parser.add_argument(
        "--function",
        help="Try to optimize only this function within the given file path",
    )
    parser.add_argument(
        "--all",
        help="Try to optimize all functions. Can take a really long time. Can pass an optional starting directory to"
        " optimize code from. If no args specified (just --all), will optimize all code in the project.",
        nargs="?",
        const="",
        default=SUPPRESS,
    )
    parser.add_argument(
        "--module-root",
        type=str,
        help="Path to the project's Python module that you want to optimize."
        " This is the top-level root directory where all the Python source code is located.",
    )
    parser.add_argument(
        "--tests-root",
        type=str,
        help="Path to the test directory of the project, where all the tests are located.",
    )
    parser.add_argument("--test-framework", choices=["pytest", "unittest"])
    parser.add_argument(
        "--config-file",
        type=str,
        help="Path to the pyproject.toml with codeflash configs.",
    )
    parser.add_argument(
        "--pytest-cmd",
        type=str,
        help="Command that codeflash will use to run pytest. If not specified, codeflash will use 'pytest'",
    )
    parser.add_argument(
        "--use-cached-tests",
        action="store_true",
        help="Use cached tests from a specified file for debugging.",
    )
    parser.add_argument("-v", "--verbose", action="store_true", help="Print verbose logs")
    args: Namespace = parser.parse_args()
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    if "command" in args and args.command == "init":
        init_codeflash()
        exit()
    if args.function and not args.file:
        raise ValueError("If you specify a --function, you must specify the --file it is in")
    if args.file:
        if not os.path.exists(args.file):
            raise ValueError(f"File {args.file} does not exist")
        args.file = os.path.realpath(args.file)

    pyproject_config = parse_config_file(args.config_file)
    supported_keys = [
        "module_root",
        "tests_root",
        "test_framework",
        "ignore_paths",
        "minimum_performance_gain",
        "pytest_cmd",
    ]
    for key in supported_keys:
        if key in pyproject_config:
            if (
                hasattr(args, key.replace("-", "_"))
                and getattr(args, key.replace("-", "_")) is None
            ) or not hasattr(args, key.replace("-", "_")):
                setattr(args, key.replace("-", "_"), pyproject_config[key])
    assert os.path.isdir(
        args.module_root
    ), f"--module-root {args.module_root} must be a valid directory"
    assert os.path.isdir(
        args.tests_root
    ), f"--tests-root {args.tests_root} must be a valid directory"
    if env_utils.get_pr_number() is not None and not env_utils.ensure_codeflash_api_key():
        assert (
            "CodeFlash API key not found. When running in a Github Actions Context, provide the "
            "'CODEFLASH_API_KEY' environment variable as a secret.\n"
            + "You can add a secret by going to your repository's settings page, then clicking 'Secrets' in the left sidebar.\n"
            + "Then, click 'New repository secret' and add your api key with the variable name CODEFLASH_API_KEY.\n"
            + f"Here's a direct link: {get_github_secrets_page_url()}\n"
            + "Exiting..."
        )
    if hasattr(args, "ignore_paths") and args.ignore_paths is not None:
        for path in args.ignore_paths:
            assert os.path.exists(
                path
            ), f"ignore-paths config must be a valid path. Path {path} does not exist"
    # Actual root path is one level above the specified directory, because that's where the module can be imported from
    args.module_root = os.path.realpath(os.path.join(args.module_root, ".."))
    args.tests_root = os.path.realpath(args.tests_root)
    args = handle_optimize_all_arg_parsing(args)
    return args


class Optimizer:
    def __init__(self, args: Namespace):
        self.args = args
        self.test_cfg = TestConfig(
            tests_root=args.tests_root,
            project_root_path=args.module_root,
            test_framework=args.test_framework,
            pytest_cmd=args.pytest_cmd,
        )

    def run(self):
        logging.info(CODEFLASH_LOGO)
        logging.info("Running optimizer.")
        if not env_utils.ensure_codeflash_api_key():
            return

        file_to_funcs_to_optimize, num_modified_functions = get_functions_to_optimize_by_file(
            optimize_all=self.args.all,
            file=self.args.file,
            function=self.args.function,
            test_cfg=self.test_cfg,
            ignore_paths=self.args.ignore_paths,
        )

        test_files_created = set()
        instrumented_unittests_created = set()
        self.found_atleast_one_optimization = False

        function_iterator_count = 0
        try:
            if num_modified_functions == 0:
                logging.info("No functions found to optimize. Exiting...")
                return
            function_to_tests: dict[str, list[TestsInFile]] = discover_unit_tests(self.test_cfg)
            logging.info(
                f"Discovered a total of {len(function_to_tests.values())} existing unit tests in the project."
            )
            for path in file_to_funcs_to_optimize:
                logging.info(f"Examining file {path} ...")
                # TODO: Sequence the functions one goes through intelligently. If we are optimizing f(g(x)), then we might want to first
                #  optimize f rather than g because optimizing f would already optimize g as it is a dependency
                with open(path, "r") as f:
                    original_code = f.read()
                for function_to_optimize in file_to_funcs_to_optimize[path]:
                    instrumented_unittests_created_for_function = set()
                    function_name = function_to_optimize.function_name
                    function_iterator_count += 1
                    logging.info(
                        f"Optimizing function {function_iterator_count} of {num_modified_functions} - {function_name}"
                    )
                    explanation_final = ""
                    winning_test_results = None
                    overall_original_test_results = None
                    if os.path.exists(get_run_tmp_file("test_return_values_0.bin")):
                        # remove left overs from previous run
                        os.remove(get_run_tmp_file("test_return_values_0.bin"))
                    if os.path.exists(get_run_tmp_file("test_return_values_0.sqlite")):
                        os.remove(get_run_tmp_file("test_return_values_0.sqlite"))
                    code_to_optimize = get_code(function_to_optimize)
                    if code_to_optimize is None:
                        logging.error("Could not find function to optimize")
                        continue

                    preexisting_functions = get_all_function_names(code_to_optimize)

                    (
                        code_to_optimize_with_dependents,
                        dependent_functions,
                    ) = get_constrained_function_context_and_dependent_functions(
                        function_to_optimize, self.args.module_root, code_to_optimize
                    )
                    logging.info("CODE TO OPTIMIZE %s", code_to_optimize_with_dependents)
                    module_path = module_name_from_file_path(path, self.args.module_root)
                    unique_original_test_files = set()
                    relevant_test_files_count = 0

                    full_module_function_path = module_path + "." + function_name
                    if full_module_function_path not in function_to_tests:
                        logging.warning(
                            "Could not find any pre-existing tests for '%s', will only use generated tests.",
                            full_module_function_path,
                        )
                    else:
                        for tests_in_file in function_to_tests.get(full_module_function_path):
                            if tests_in_file.test_file in unique_original_test_files:
                                continue
                            relevant_test_files_count += 1
                            injected_test = inject_profiling_into_existing_test(
                                tests_in_file.test_file,
                                function_name,
                                self.args.module_root,
                            )
                            new_test_path = (
                                os.path.splitext(tests_in_file.test_file)[0]
                                + "__perfinstrumented"
                                + os.path.splitext(tests_in_file.test_file)[1]
                            )
                            with open(new_test_path, "w") as f:
                                f.write(injected_test)
                            instrumented_unittests_created.add(new_test_path)
                            instrumented_unittests_created_for_function.add(new_test_path)
                            unique_original_test_files.add(tests_in_file.test_file)
                        logging.info(
                            f"Discovered {relevant_test_files_count} existing unit test file"
                            f"{'s' if relevant_test_files_count > 1 else ''} for {full_module_function_path}"
                        )

                    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
                        # Newly generated tests (not instrumented yet)
                        future_tests = executor.submit(
                            self.generate_and_instrument_tests,
                            code_to_optimize_with_dependents,
                            function_to_optimize,
                            [definition.full_name for definition in dependent_functions],
                            module_path,
                        )
                        future_optimization = executor.submit(
                            optimize_python_code,
                            code_to_optimize_with_dependents,
                            N_CANDIDATES,
                        )

                        future_tests_result = future_tests.result()
                        optimizations = future_optimization.result()
                    if (
                        future_tests_result
                        and isinstance(future_tests_result, tuple)
                        and len(future_tests_result) == 2
                    ):
                        (
                            generated_original_test_source,
                            instrumented_test_source,
                        ) = future_tests_result
                    else:
                        logging.error(
                            "/!\\ NO TESTS GENERATED for %s", function_to_optimize.function_name
                        )
                        continue

                    generated_tests_path = get_test_file_path(
                        self.args.tests_root, function_to_optimize.function_name, 0
                    )
                    with open(generated_tests_path, "w") as file:
                        file.write(instrumented_test_source)

                    test_files_created.add(generated_tests_path)
                    original_runtime = None
                    times_run = 0
                    # TODO : Dynamically determine the number of times to run the tests based on the runtime of the tests.
                    # Keep the runtime in some acceptable range
                    generated_tests_elapsed_time = 0.0

                    # For the original function - run the tests and get the runtime
                    # TODO: Compare the function return values over the multiple runs and check if they are any different,
                    #  if they are different, then we can't optimize this function because it is a non-deterministic function
                    test_env = os.environ.copy()
                    test_env["CODEFLASH_TEST_ITERATION"] = str(0)
                    for i in range(MAX_TEST_RUN_ITERATIONS):
                        if generated_tests_elapsed_time > MAX_FUNCTION_TEST_SECONDS:
                            break
                        instrumented_test_timing = []
                        original_test_results_iter = TestResults()
                        for test_file in instrumented_unittests_created_for_function:
                            unittest_results = self.run_and_parse_tests(
                                test_env, test_file, TestType.EXISTING_UNIT_TEST, 0
                            )

                            timing = unittest_results.total_passed_runtime()
                            original_test_results_iter.merge(unittest_results)
                            instrumented_test_timing.append(timing)
                        if i == 0:
                            logging.info(
                                f"original code, existing unit test results -> {original_test_results_iter.get_test_pass_fail_report()}"
                            )

                        original_gen_results = self.run_and_parse_tests(
                            test_env, generated_tests_path, TestType.GENERATED_REGRESSION, 0
                        )

                        # TODO: Implement the logic to disregard the timing info of the tests that ERRORed out. That is remove test cases that failed to run.

                        if not original_gen_results and len(instrumented_test_timing) == 0:
                            logging.warning(
                                f"Couldn't run any tests for original function {function_name}. SKIPPING OPTIMIZING THIS FUNCTION."
                            )

                            break
                        # TODO: Doing a simple sum of test runtime, Improve it by looking at test by test runtime, or a better scheme
                        # TODO: If the runtime is None, that happens in the case where an exception is expected and is successfully
                        #  caught by the test framework. This makes the test pass, but we can't find runtime because the exception caused
                        #  the execution to not reach the runtime measurement part. We are currently ignoring such tests, because the performance
                        #  for such a execution that raises an exception should not matter.
                        if i == 0:
                            logging.info(
                                f"original generated tests results -> {original_gen_results.get_test_pass_fail_report()}"
                            )

                        original_total_runtime_iter = (
                            original_gen_results.total_passed_runtime()
                            + sum(instrumented_test_timing)
                        )
                        if original_total_runtime_iter == 0:
                            logging.warning(
                                f"The overall test runtime of the original function is 0, trying again..."
                            )
                            logging.warning(original_gen_results.test_results)
                            continue
                        original_test_results_iter.merge(original_gen_results)
                        if i == 0:
                            logging.info(
                                f"Original overall test results = {TestResults.report_to_string(original_test_results_iter.get_test_pass_fail_report_by_type())}"
                            )
                        if (
                            original_runtime is None
                            or original_total_runtime_iter < original_runtime
                        ):
                            original_runtime = best_runtime = original_total_runtime_iter
                            overall_original_test_results = original_test_results_iter

                        times_run += 1

                    if times_run == 0:
                        logging.warning(
                            "Failed to run the tests for the original function, skipping optimization"
                        )
                        continue
                    logging.info(
                        f"ORIGINAL CODE RUNTIME OVER {times_run} RUN{'S' if times_run > 1 else ''} = {original_runtime}ns"
                    )
                    logging.info("OPTIMIZING CODE....")
                    # TODO: Postprocess the optimized function to include the original docstring and such

                    best_optimization = []
                    for i, (optimized_code, explanation) in enumerate(optimizations):
                        j = i + 1
                        if optimized_code is None:
                            continue
                        if os.path.exists(get_run_tmp_file(f"test_return_values_{j}.bin")):
                            # remove left overs from previous run
                            os.remove(get_run_tmp_file(f"test_return_values_{j}.bin"))
                        if os.path.exists(get_run_tmp_file(f"test_return_values_{j}.sqlite")):
                            os.remove(get_run_tmp_file(f"test_return_values_{j}.sqlite"))
                        logging.info(f"Optimized Candidate:")
                        logging.info(optimized_code)
                        try:
                            new_code = replace_function_in_file(
                                path,
                                function_name,
                                optimized_code,
                                preexisting_functions,
                                # test_cfg.project_root_path,
                                # function_dependencies,
                            )
                        except (
                            ValueError,
                            SyntaxError,
                            cst.ParserSyntaxError,
                            AttributeError,
                        ) as e:
                            logging.error(e)
                            continue
                        with open(path, "w") as f:
                            f.write(new_code)
                        all_test_times = []
                        equal_results = True
                        generated_tests_elapsed_time = 0.0

                        times_run = 0
                        test_env = os.environ.copy()
                        test_env["CODEFLASH_TEST_ITERATION"] = str(j)
                        for test_index in range(MAX_TEST_RUN_ITERATIONS):
                            if os.path.exists(get_run_tmp_file(f"test_return_values_{j}.bin")):
                                os.remove(get_run_tmp_file(f"test_return_values_{j}.bin"))
                            if os.path.exists(get_run_tmp_file(f"test_return_values_{j}.sqlite")):
                                os.remove(get_run_tmp_file(f"test_return_values_{j}.sqlite"))
                            if generated_tests_elapsed_time > MAX_FUNCTION_TEST_SECONDS:
                                break

                            optimized_test_results_iter = TestResults()
                            instrumented_test_timing = []
                            for (
                                instrumented_test_file
                            ) in instrumented_unittests_created_for_function:
                                unittest_results_optimized = self.run_and_parse_tests(
                                    test_env, instrumented_test_file, TestType.EXISTING_UNIT_TEST, j
                                )
                                timing = unittest_results_optimized.total_passed_runtime()
                                optimized_test_results_iter.merge(unittest_results_optimized)
                                instrumented_test_timing.append(timing)
                            if test_index == 0:
                                equal_results = True
                                logging.info(
                                    f"optimized existing unit tests result -> {optimized_test_results_iter.get_test_pass_fail_report()}"
                                )
                                for test_invocation in optimized_test_results_iter:
                                    if (
                                        overall_original_test_results.get_by_id(test_invocation.id)
                                        is None
                                        or test_invocation.did_pass
                                        != overall_original_test_results.get_by_id(
                                            test_invocation.id
                                        ).did_pass
                                    ):
                                        logging.info("RESULTS DID NOT MATCH")
                                        logging.info(
                                            f"Test {test_invocation.id} failed on the optimized code. Skipping this optimization"
                                        )
                                        equal_results = False
                                        break
                                if not equal_results:
                                    break

                            test_results = self.run_and_parse_tests(
                                test_env, generated_tests_path, TestType.GENERATED_REGRESSION, j
                            )

                            if test_index == 0:
                                logging.info(
                                    f"generated test_results optimized -> {test_results.get_test_pass_fail_report()}"
                                )
                                if test_results:
                                    if compare_results(original_gen_results, test_results):
                                        equal_results = True
                                        logging.info("RESULTS MATCHED!")
                                    else:
                                        logging.info("RESULTS DID NOT MATCH")
                                        equal_results = False
                            if not equal_results:
                                break

                            test_runtime = test_results.total_passed_runtime() + sum(
                                instrumented_test_timing
                            )

                            if test_runtime == 0:
                                logging.warning(
                                    f"The overall test runtime of the optimized function is 0, trying again..."
                                )
                                continue
                            all_test_times.append(test_runtime)
                            optimized_test_results_iter.merge(test_results)
                            times_run += 1
                        if os.path.exists(get_run_tmp_file(f"test_return_values_{j}.bin")):
                            os.remove(get_run_tmp_file(f"test_return_values_{j}.bin"))
                        if os.path.exists(get_run_tmp_file(f"test_return_values_{j}.sqlite")):
                            os.remove(get_run_tmp_file(f"test_return_values_{j}.sqlite"))
                        if equal_results and times_run > 0:
                            new_test_time = min(all_test_times)

                            original_runtime_human = humanize_runtime(original_runtime)
                            new_test_time_human = humanize_runtime(new_test_time)

                            logging.info(
                                f"NEW CODE RUNTIME OVER {times_run} RUN{'S' if times_run > 1 else ''} = {new_test_time_human}, SPEEDUP RATIO = {((original_runtime - new_test_time) / new_test_time):.3f}"
                            )
                            if (
                                ((original_runtime - new_test_time) / new_test_time)
                                > self.args.minimum_performance_gain
                            ) and new_test_time < best_runtime:
                                logging.info("THIS IS BETTER!")

                                logging.info(
                                    f"original_test_time={original_runtime_human} new_test_time={new_test_time_human}, FASTER RATIO = {((original_runtime - new_test_time) / new_test_time)}"
                                )
                                best_optimization = [optimized_code, explanation]
                                best_runtime = new_test_time
                                winning_test_results = optimized_test_results_iter
                        with open(path, "w") as f:
                            f.write(original_code)
                        logging.info("----------------")
                    logging.info(f"BEST OPTIMIZATION {best_optimization}")
                    if best_optimization:
                        self.found_atleast_one_optimization = True
                        logging.info(f"BEST OPTIMIZED CODE\n{best_optimization[0]}")

                        new_code = replace_function_in_file(
                            path,
                            function_name,
                            best_optimization[0],
                            preexisting_functions,
                            # test_cfg.project_root_path,
                            # function_dependencies,
                        )
                        with open(path, "w") as f:
                            f.write(new_code)
                        # TODO: After doing the best optimization, remove the test cases that errored on the new code, because they might be failing because of syntax errors and such.
                        speedup = (original_runtime / best_runtime) - 1
                        # TODO: Sometimes the explanation says something similar to "This is the code that was optimized", remove such parts

                        explanation_final += (
                            f"Function {function_name} in file {path}:\n"
                            f"Performance went up by {speedup:.2f}x ({speedup * 100:.2f}%). Runtime went down from {original_runtime_human} to {new_test_time_human} \n\n"
                            + "Optimization explanation:\n"
                            + best_optimization[1]
                            + " \n\n"
                            + "The code has been tested for correctness.\n"
                            + f"Test Results for the best optimized code:- {TestResults.report_to_string(winning_test_results.get_test_pass_fail_report_by_type())}\n"
                        )
                        logging.info(f"EXPLANATION_FINAL\n{explanation_final}")

                        logging.info("Formatting code with black...")
                        # black currently does not have a stable public API, so we are using the CLI
                        # the main problem is custom config parsing https://github.com/psf/black/issues/779
                        result = subprocess.run(
                            ["black", path], stdout=subprocess.PIPE, stderr=subprocess.PIPE
                        )
                        if result.returncode == 0:
                            logging.info("OK")
                            with open(path, "r") as f:
                                new_code = f.read()
                        else:
                            logging.error("Failed to format")
                        logging.info(
                            f"Optimization was validated for correctness by running the following test - \n{generated_original_test_source}"
                        )

                        logging.info(
                            f"⚡️ Optimization successful! 📄 {function_name} in {path} 📈 {speedup * 100:.2f}% ({speedup:.2f}x) faster"
                        )

                        pr: Optional[int] = env_utils.get_pr_number()

                        if pr is not None:
                            logging.info(f"Suggesting changes to PR #{pr} ...")

                            owner, repo = get_repo_owner_and_name()
                            relative_path = os.path.relpath(path, git_root_dir())
                            response = cfapi.suggest_changes(
                                owner=owner,
                                repo=repo,
                                pr_number=pr,
                                file_changes={
                                    relative_path: FileDiffContent(
                                        oldContent=original_code, newContent=new_code
                                    ).model_dump(mode="json")
                                },
                                pr_comment=PrComment(
                                    optimization_explanation=best_optimization[1],
                                    best_runtime=best_runtime,
                                    original_runtime=original_runtime,
                                    function_name=function_name,
                                    relative_file_path=relative_path,
                                    speedup=speedup,
                                    winning_test_results=winning_test_results,
                                ),
                                generated_tests=generated_original_test_source,
                            )
                            if response.ok:
                                logging.info("OK")
                            else:
                                logging.error(
                                    f"Optimization was successful, but I failed to suggest changes to PR #{pr}."
                                    f" Response from server was: {response.text}"
                                )
                        elif self.args.all:
                            logging.info("Creating a new PR with the optimized code...")
                            owner, repo = get_repo_owner_and_name()

                            relative_path = os.path.relpath(path, git_root_dir())
                            base_branch = get_current_branch()
                            response = cfapi.create_pr(
                                owner=owner,
                                repo=repo,
                                base_branch=base_branch,
                                file_changes={
                                    relative_path: FileDiffContent(
                                        oldContent=original_code, newContent=new_code
                                    ).model_dump(mode="json")
                                },
                                pr_comment=PrComment(
                                    optimization_explanation=best_optimization[1],
                                    best_runtime=best_runtime,
                                    original_runtime=original_runtime,
                                    function_name=function_name,
                                    relative_file_path=relative_path,
                                    speedup=speedup,
                                    winning_test_results=winning_test_results,
                                ),
                                generated_tests=generated_original_test_source,
                            )
                            if response.ok:
                                logging.info("OK")
                            else:
                                logging.error(
                                    f"Optimization was successful, but I failed to create a PR with the optimized code."
                                    f" Response from server was: {response.text}"
                                )
                            # Reverting to original code, because optimizing functions in a sequence can lead to
                            #  a. Error propagation, where error in one function can cause the next optimization to fail
                            #  b. Performance estimates become unstable, as the runtime of an optimization might be
                            #     dependent on the runtime of the previous optimization
                            with open(path, "w") as f:
                                f.write(original_code)
                    # Delete all the generated tests to not cause any clutter.
                    if os.path.exists(generated_tests_path):
                        os.remove(generated_tests_path)
                    for test_paths in instrumented_unittests_created_for_function:
                        if os.path.exists(test_paths):
                            os.remove(test_paths)
            if not self.found_atleast_one_optimization:
                logging.info(f"❌ No optimizations found.")

        finally:
            # TODO: Also revert the file/function being optimized if the process did not succeed
            for test_file in instrumented_unittests_created:
                if os.path.exists(test_file):
                    os.remove(test_file)
            for test_file in test_files_created:
                if os.path.exists(test_file):
                    os.remove(test_file)
            if hasattr(get_run_tmp_file, "tmpdir"):
                get_run_tmp_file.tmpdir.cleanup()

    def run_and_parse_tests(
        self,
        test_env: dict[str, str],
        test_file: str,
        test_type: TestType,
        optimization_iteration: int,
    ) -> TestResults:
        result_file_path, run_result = run_tests(
            test_file,
            test_framework=self.args.test_framework,
            cwd=self.args.module_root,
            pytest_timeout=INDIVIDUAL_TEST_TIMEOUT,
            pytest_cmd=self.test_cfg.pytest_cmd,
            verbose=True,
            test_env=test_env,
        )
        unittest_results = parse_test_results(
            test_xml_path=result_file_path,
            test_py_path=test_file,
            test_config=self.test_cfg,
            test_type=test_type,
            run_result=run_result,
            optimization_iteration=optimization_iteration,
        )
        return unittest_results

    def generate_and_instrument_tests(
        self,
        source_code_being_tested: str,
        function_to_optimize: FunctionToOptimize,
        dependent_function_names: list[str],
        module_path: str,
    ) -> Union[Tuple[str, str], None]:
        response = generate_tests(
            source_code_being_tested=source_code_being_tested,
            function_to_optimize=function_to_optimize,
            dependent_function_names=dependent_function_names,
            module_path=module_path,
            test_cfg=self.test_cfg,
            test_timeout=INDIVIDUAL_TEST_TIMEOUT,
            use_cached_tests=self.args.use_cached_tests,
        )
        if response is None:
            logging.error(
                f"Failed to generate and instrument tests for {function_to_optimize.function_name}"
            )
            return None

        generated_original_test_source, instrumented_test_source = response

        return generated_original_test_source, instrumented_test_source


def main():
    """Entry point for the codeflash command-line interface."""
    Optimizer(parse_args()).run()


if __name__ == "__main__":
    main()
