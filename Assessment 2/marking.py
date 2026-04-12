"""
This file performs the actual unit testing of the students code.
"""

import importlib.util
import math
import multiprocessing
import numbers
import traceback
from dataclasses import dataclass, fields
from pathlib import Path
from typing import Any, Callable, Optional

UNIT_TEST_FILE_NAME = "unit_tests.py"
UNIT_TEST_VARIABLE_NAME = "UNIT_TESTS"

MATPLOTLIB_OUTPUT_TYPES = {
    "Figure",
    "Axes",
}

# Types that we don't ever want to send across processes (they are slow to pickle)
SLOW_OUTPUT_TYPES = {*MATPLOTLIB_OUTPUT_TYPES}


# Ideally this would be in its own file but to keep this file self-contained placing it here
@dataclass
class StudentSubmission:
    name_prefix: str  # The first and last names combined as Canvas formats it
    id: str  # Canvas puts files in the form studentname_[id]_numbers_Q1.py. This is the [id]
    submitted_files: list[Path]


@dataclass
class UnitTestResult:
    function_name: str
    input: list[Any]  # The input arguments can be anything we specify
    expected: Any  # The expected output can be anything we specify
    actual: Optional[Any]  # The actual output of the function
    passed: bool  # Whether the test passed
    error: Optional[Exception]
    traceback: Optional[str]
    feedback: Optional[
        str
    ]  # This is to allow markers to put the feedback in our own unit tests to generate for students
    mark_for_pass: Optional[float]  # How many marks are awarded if the test passes


@dataclass
class ExpectedAnswerValidator:
    """
    Wraps a validation function for pickling compatibility on Windows. Windows
    does not fork the current process when using multiprocessing, instead it
    spawns a new Python interpreter. So passing functions between these
    processes is awkward. Instead we just ask the subprocess to import the
    required modules through this wrapper type
    """

    module_name: str
    function_name: str
    expected_string: Optional[str] = (
        None  # If the validation function returns some "expected" output for student feedback. We will store it here.
    )

    def resolve(self) -> Callable:
        """
        Resolves the function to its actual callable. Note this can fail but
        not in the way we use it here. We create this based on an already
        loaded module. Then reload it again when running the unit tests. So if
        it was going to fail it would fail on the initial resolve.
        """
        module = importlib.import_module(self.module_name)
        return getattr(module, self.function_name)


@dataclass
class SlowDataType:
    """
    This is used when sending a given data type over IPC would be slow. So for
    example plots from matplotlib would be slow. In this case we just simply
    print the name of the class rather than trying to print all information
    about the data type.
    """

    fully_qualified_name: str


@dataclass
class UnitTest:
    question: str
    function_name: str
    input: list[Any]
    expected: Any
    feedback: Optional[str] = None
    mark: Optional[float] = (
        None  # How much this unit test is worth. Not supplied to students
    )
    float_tolerance: float = 1e-9

    def __post_init__(self):
        if not isinstance(self.question, str):
            raise TypeError(
                "Please ensure that the dictionary key 'question' is a string such as Q1 etc."
            )
        if not isinstance(self.function_name, str):
            raise TypeError(
                "Please ensure that the dictionary key 'function_name' is a string."
            )
        if callable(self.expected):
            expected_func = self.expected
            self.expected = ExpectedAnswerValidator(
                module_name=expected_func.__module__,
                function_name=expected_func.__name__,
            )


def load_unit_tests(unit_test_file: Path) -> dict[str, list[UnitTest]]:
    """
    Returns all the unit tests loaded from the file. It formats this as a
    dictionary mapping the question name to a list of the unit tests associated
    with that question
    """

    if not unit_test_file.exists():
        raise Exception(
            f"Could not find unit test file. Please ensure that the unit test file is in the current directory with the name '{UNIT_TEST_FILE_NAME}'"
        )

    spec = importlib.util.spec_from_file_location(unit_test_file.stem, unit_test_file)
    if spec is None or spec.loader is None:
        raise Exception(f"Failed to open unit test file at path: {unit_test_file}")

    module = importlib.util.module_from_spec(spec)
    if module is None:
        raise Exception(
            "Failed to load unit tests. Please ensure that the syntax is correct."
        )

    try:
        spec.loader.exec_module(module)
    except Exception as e:
        raise Exception(
            f"Failed to parse unit test python module. Please ensure all of the python code is correct. \n\tReceived error: {e}"
        ) from e

    try:
        unit_test_dicts = getattr(module, UNIT_TEST_VARIABLE_NAME)
    except AttributeError:
        raise AttributeError(
            f"Failed to load the unit tests. Please ensure that the variable is named '{UNIT_TEST_VARIABLE_NAME}' and is a list of dictionaries"
        )

    if not isinstance(unit_test_dicts, list) or not all(
        isinstance(d, dict) for d in unit_test_dicts
    ):
        raise TypeError(f"'{UNIT_TEST_VARIABLE_NAME}' must be a list of dictionaries")

    return unit_tests_from_dicts(unit_test_dicts)


def unit_tests_from_dicts(unit_test_dicts: list[dict]) -> dict[str, list[UnitTest]]:
    """
    Turns a list of unit tests into a dictionary mapping the question name to a
    list of the unit tests associated with that question.
    Converts callable 'expected' values to ExpectedAnswerValidator for pickling
    compatibility.
    """
    unit_tests: dict[str, list[UnitTest]] = {}
    for i, test in enumerate(unit_test_dicts):
        try:
            if not isinstance(test, dict):
                raise TypeError(f"Expected dict, got {type(test).__name__}")
            test_copy = test.copy()
            if callable(test_copy.get("expected")):
                expected_func = test_copy["expected"]
                test_copy["expected"] = ExpectedAnswerValidator(
                    module_name=expected_func.__module__,
                    function_name=expected_func.__name__,
                )
            ut = UnitTest(**test_copy)
            if ut.question in unit_tests:
                unit_tests[ut.question].append(ut)
            else:
                unit_tests[ut.question] = [ut]

        except TypeError as e:
            field_names = ", ".join(f'"{f.name}"' for f in fields(UnitTest))
            raise TypeError(
                f"Failed to load unit test at index {i}: {repr(test)}. "
                f"Please only define unit tests with the keys: {field_names}\n\tReceived error: {e}"
            )

    return unit_tests


def run_all_unit_tests(
    submission: StudentSubmission,
    unit_tests: dict[str, list[UnitTest]],
    timeout_per_question_sec: float,
) -> dict[str, list[UnitTestResult]]:
    """
    Runs the students submission against all defined unit tests.
    """

    results = {}
    for question, tests in unit_tests.items():
        test_result = run_unit_tests_for_question(
            submission, question, tests, timeout_per_question_sec
        )

        assert question not in results, (
            "We should run all tests per question in one go."
        )
        results[question] = test_result

    return results


def get_files_for_question(files: list[Path], question: str) -> list[Path]:
    files_that_match = []
    for file in files:
        if question in file.stem:
            files_that_match.append(file)

    if len(files_that_match) > 1:
        # If a student uploads a new version of the same file, Canvas will
        # append "-[number]" to the end of the file name. Where number
        # increments by one for each new upload. The way to handle this is to
        # accept the file that has the largest "[number]" as this is the
        # students latest submission
        latest_uploaded_file: Optional[Path] = None
        current_largest_num = -1
        for file in files_that_match:
            # eg. studentname_12341_1234_Q1-1.py => ["studentname_12341_1234_Q1", "-1"]
            parts = file.stem.split(question)
            upload_number = parts[-1].lstrip("-")
            if upload_number != "":
                try:
                    num = int(upload_number)
                    if num > current_largest_num:
                        current_largest_num = num
                        latest_uploaded_file = file
                except Exception as _:
                    # We could not convert the file. This means either the
                    # student has named the file in a strange way or Canvas has
                    # changed their naming scheme. We will just continue with
                    # all files in this case.
                    return files_that_match
        if latest_uploaded_file is not None:
            # Return only the file we have filtered for
            return [latest_uploaded_file]

    return files_that_match


def run_unit_tests_for_question(
    submission: StudentSubmission,
    question: str,
    unit_tests: list[UnitTest],
    timeout_sec: float,
) -> list[UnitTestResult]:
    files = get_files_for_question(submission.submitted_files, question)
    if len(files) == 0:
        return [
            UnitTestResult(
                function_name=test.function_name,
                input=test.input,
                expected=test.expected,
                actual=None,
                error=Exception(
                    f"Could not find a file for Question: {question}. Please make sure the file ends in {question}.py"
                ),
                traceback=None,
                passed=False,
                feedback=test.feedback,
                mark_for_pass=test.mark,
            )
            for test in unit_tests
        ]
    if len(files) > 1:
        raise Exception(
            f"Found multiple submitted files that match the question: '{question}' for student: '{submission.name_prefix}'"
        )

    file = files[0]  # Should only have one file

    queue = multiprocessing.Queue()
    p = multiprocessing.Process(
        target=unit_test_run_worker, args=(file, unit_tests, queue)
    )
    p.start()
    p.join(timeout_sec)
    if p.is_alive():
        p.terminate()  # Kill the process if we timed out but still running
        p.join()
        return [
            UnitTestResult(
                function_name=test.function_name,
                input=test.input,
                expected=test.expected,
                actual=None,
                error=Exception(
                    f"The code took too long to run all of the tests for question {question}. Please check you are not stuck in a loop somewhere."
                ),
                traceback=None,
                passed=False,
                feedback=test.feedback,
                mark_for_pass=test.mark,
            )
            for test in unit_tests
        ]

    # Process finished correctly
    try:
        unit_test_results = queue.get_nowait()
    except Exception as e:
        raise Exception(
            f"Failed to retrieve items from process queue. Please contact ENGG1003 lab demonstrator about this as it should not be possible. Failed with error: {repr(e)}"
        )

    for ut in unit_test_results:
        if isinstance(ut.error, IncorrectUnitTestExpectedFunction):
            raise ut.error
    return unit_test_results


def deep_equal(expected, actual, tol: float) -> bool:
    # Handle numpy arrays by converting them to lists
    if hasattr(expected, "tolist"):
        expected = expected.tolist()
    if hasattr(actual, "tolist"):
        actual = actual.tolist()

    if isinstance(expected, numbers.Number) and isinstance(actual, numbers.Number):
        return math.isclose(expected, actual, rel_tol=tol, abs_tol=tol)  # pyright: ignore

    if isinstance(expected, (list, tuple)) and isinstance(actual, (list, tuple)):
        if len(expected) != len(actual):
            return False
        return all(deep_equal(e, a, tol=tol) for e, a in zip(expected, actual))

    return expected == actual


class IncorrectUnitTestExpectedFunction(Exception):
    """Raised when the unit test expected function defined in the unit test file is not returning the correct dictionary and keys"""

    pass


def unit_test_run_worker(
    student_file: Path, unit_tests: list[UnitTest], queue: multiprocessing.Queue
):
    """
    This function is intended to be called as a worker, that is, it should be
    spawned into another process and run. That way we can timeout etc for
    students code.
    """

    try:
        if not student_file.exists():
            raise Exception(
                f"Could not find the file '{student_file}'. Please ensure that the file has the correct name and path."
            )

        spec = importlib.util.spec_from_file_location(student_file.stem, student_file)
        if spec is None or spec.loader is None:
            raise Exception(f"Failed to open file at path: '{student_file}'")

        student_module = importlib.util.module_from_spec(spec)
        if student_module is None:
            raise Exception(
                f"Failed to load the python code in '{student_file}'. Please ensure that the syntax is correct."
            )

        try:
            spec.loader.exec_module(student_module)
        except Exception as e:
            raise Exception(
                f"Failed to load students code. Please ensure all of the python code is correct. \n\tReceived error: {e}"
            ) from e
    except Exception as e:
        # We failed to load the students code. All of the test results will have the error provided from the try block as the result.
        results = [
            UnitTestResult(
                function_name=test.function_name,
                input=test.input,
                expected=None,
                actual=None,
                error=e,
                traceback=traceback.format_exc(),
                passed=False,
                feedback=test.feedback,
                mark_for_pass=test.mark,  # Get mark of zero if we could not load the code
            )
            for test in unit_tests
        ]
        queue.put(results)
        queue.close()
        queue.join_thread()
        return

    results = []
    for test in unit_tests:
        # We have successfully loaded the module. Now run the tests.
        try:
            student_func = getattr(student_module, test.function_name)
        except AttributeError as _:
            # The student did not have a function of the correct name
            results.append(
                UnitTestResult(
                    function_name=test.function_name,
                    input=test.input,
                    expected=None,
                    actual=None,
                    error=Exception(
                        f"Could not find function '{test.function_name}' in the file '{student_file}'. Please double check the name of the function we wish to test."
                    ),
                    traceback=None,
                    passed=False,
                    feedback=test.feedback,
                    mark_for_pass=test.mark,
                )
            )
            continue

        try:
            output = student_func(*test.input)

            if isinstance(test.expected, ExpectedAnswerValidator):
                expected_func = test.expected.resolve()
                test_func_output = expected_func(output)
                if not (
                    type(test_func_output) is dict
                    and "passed" in test_func_output.keys()
                    and "expected" in test_func_output.keys()
                ):
                    test.expected = None
                    raise IncorrectUnitTestExpectedFunction(
                        "If we are using a function to check whether or not a test failed then we must return a dict with two fields 'passed' which is either True or False, and 'expected' which indicates what we expected the answer to be, or what just a message that should be shown to the students"
                    )
                passed = test_func_output["passed"]
                test.expected.expected_string = test_func_output["expected"]

            else:
                passed = deep_equal(test.expected, output, tol=test.float_tolerance)

            if output_contains_slow_type(output, SLOW_OUTPUT_TYPES):
                # This type is known to be slow for IPC so we just print
                # the name of the class
                output = SlowDataType(fully_qualified_name(output))

            results.append(
                UnitTestResult(
                    function_name=test.function_name,
                    input=test.input,
                    expected=test.expected,
                    actual=output,
                    error=None,
                    traceback=None,
                    passed=passed,
                    feedback=test.feedback,
                    mark_for_pass=test.mark,
                )
            )
        except Exception as e:
            # The students code crashed just for this particular input

            error = e
            tb = traceback.format_exc()
            passed = False
            actual = None

            if isinstance(test.expected, Exception):
                # We expected to have thrown an error during this test
                if (type(test.expected) is type(e)) and (str(test.expected) == str(e)):
                    # The student raised the correct error so clear error messages and give pass
                    error = None
                    tb = None
                    actual = e  # The actual thing we want to test is the exception that was returned
                    passed = True
                else:
                    # The student raised an error but it wasn't correct, keep
                    # the error and traceback incase it is for an actual bug

                    actual = e  # The actual thing we want to test is the exception that was returned
                    passed = False

            results.append(
                UnitTestResult(
                    function_name=test.function_name,
                    input=test.input,
                    expected=test.expected,
                    actual=actual,
                    error=error,
                    traceback=tb,
                    passed=passed,
                    feedback=test.feedback,
                    mark_for_pass=test.mark,  # The code threw an error so 0
                )
            )

    queue.put(results)
    queue.close()
    queue.join_thread()

    return


def print_unit_test_results(unit_test_results: dict[str, list[UnitTestResult]]):
    # Sort questions
    sorted_results = dict(sorted(unit_test_results.items()))

    total_passed = 0
    total_failed = 0

    for question, results in sorted_results.items():
        print(f"\n=== Question {question} Results ===")

        question_passed = 0
        question_failed = 0

        for result in results:
            input_args_str = ", ".join(
                [f"{str(arg)} : {type(arg).__name__}" for arg in result.input]
            )
            if result.passed:
                print(f"  ✅ {result.function_name}({input_args_str}) → PASSED")
                question_passed += 1
            else:
                print(f"  ❌ {result.function_name}({input_args_str}) → FAILED")
                question_failed += 1

            print_result(result, result.passed)

        # Summary per question
        print(
            f"  → Question {question} Summary: {question_passed} passed, {question_failed} failed"
        )
        total_passed += question_passed
        total_failed += question_failed

    # Overall summary
    print("\n=== Overall Summary ===")
    print(f"Total Passed: {total_passed}")
    print(f"Total Failed: {total_failed}")


def print_result(result: UnitTestResult, passed: bool):
    if passed:
        # If they passed just show what their function returned so they can check themselves
        if isinstance(result.actual, Exception):
            print(f"     Returned exception: {exception_repr(result.actual)}")
        elif isinstance(result.actual, SlowDataType):
            print(f"     Returned:   {result.actual.fully_qualified_name}")
        else:
            print(
                f"     Returned:   {result.actual} (type: {type(result.actual).__name__})"
            )
        return

    if isinstance(result.expected, Exception):
        print(f"     Expected the exception: {exception_repr(result.expected)}")
    elif isinstance(result.expected, ExpectedAnswerValidator):
        if result.expected.expected_string is not None:
            print(
                f'     Expected: "{result.expected.expected_string}" - Validated by function: {result.expected.module_name}.{result.expected.function_name}'
            )
    else:
        print(
            f"     Expected: {result.expected} (type: {type(result.expected).__name__})"
        )

    if isinstance(result.actual, Exception):
        print(f"     Actual exception: {exception_repr(result.actual)}")
    elif isinstance(result.actual, SlowDataType):
        print(f"     Actual: {result.actual.fully_qualified_name}")
    else:
        print(f"     Actual:   {result.actual} (type: {type(result.actual).__name__})")

    if result.feedback:
        print(f"     Feedback: {result.feedback}")
    if result.error:
        print(f"     Error: {str(result.error)}")
    if result.traceback:
        print("     Traceback:")
        for line in result.traceback.splitlines():
            print(f"       {line}")


def exception_repr(exc: BaseException) -> str:
    cls_name = exc.__class__.__name__

    if not exc.args:
        return f"{cls_name}()"
    if len(exc.args) == 1:
        return f"{cls_name}({exc.args[0]!r})"

    return f"{cls_name}({', '.join(repr(a) for a in exc.args)})"


def fully_qualified_name(obj, *, max_items=5, max_depth=3, _depth=0):
    CONTAINER_TYPES = (tuple, list, set, frozenset)
    base = type(obj).__name__

    # Stop recursion if max depth reached or not a container
    if _depth >= max_depth or not isinstance(obj, CONTAINER_TYPES):
        return base

    try:
        items = list(obj)[:max_items]
    except TypeError:
        return base

    if not items:
        return f"{base}[]"

    subtypes = [
        fully_qualified_name(
            item, max_items=max_items, max_depth=max_depth, _depth=_depth + 1
        )
        for item in items
    ]
    inner = ", ".join(subtypes)
    return f"{base}[{inner}]"


def output_contains_slow_type(output, slow_types, max_items=100):
    stack = [output]
    seen = set()
    checked = 0

    while stack and checked < max_items:
        obj = stack.pop()
        oid = id(obj)
        if oid in seen:
            continue
        seen.add(oid)
        checked += 1

        if fully_qualified_name(obj) in slow_types:
            return True

        if isinstance(obj, (list, tuple, set, frozenset)):
            stack.extend(obj)

    return False


def unit_test_returned_matplotlib_plot(actual_test_output: Any) -> bool:
    if isinstance(actual_test_output, SlowDataType) and any(
        [
            matplot_lib_type in actual_test_output.fully_qualified_name
            for matplot_lib_type in MATPLOTLIB_OUTPUT_TYPES
        ]
    ):
        return True
    return False


if __name__ == "__main__":
    import glob
    import os

    cwd = Path(os.getcwd())
    unit_test_file_path = cwd.joinpath(UNIT_TEST_FILE_NAME)
    unit_tests = load_unit_tests(unit_test_file_path)

    current_file = Path(__file__).resolve()

    files = []
    for file in glob.glob(str(cwd.joinpath("*.py"))):
        if file in {current_file, unit_test_file_path.resolve()}:
            continue
        files.append(Path(file))

    submission = StudentSubmission(name_prefix="", id="", submitted_files=files)
    unit_test_results = run_all_unit_tests(
        submission, unit_tests, timeout_per_question_sec=5
    )

    print_unit_test_results(unit_test_results=unit_test_results)

    # Show the students any plots they created so they can debug it.
    for question, results in unit_test_results.items():
        prev_plotted_function = None
        for result in results:
            # Make sure the result has no errors, is actually plotting
            # something, and has not already been plotted
            if (
                result.error is None
                and unit_test_returned_matplotlib_plot(result.actual)
                and result.function_name != prev_plotted_function
            ):
                # Remember the function name so we don't replot it.
                prev_plotted_function = result.function_name

                # Dynamically import matplotlib as we will need it for showing
                # the students plots
                plt = importlib.import_module("matplotlib.pyplot")
                file = get_files_for_question(submission.submitted_files, question)[0]
                spec = importlib.util.spec_from_file_location(file.stem, file)
                if spec is None or spec.loader is None:
                    print(
                        f"Failed to load students file spec for question {question}. Make sure there are no syntax errors in the file"
                    )
                    continue

                student_module = importlib.util.module_from_spec(spec)
                if student_module is None:
                    print(
                        f"Failed to load students module for question {question}. Make sure there are no syntax errors in the file"
                    )
                    continue

                spec.loader.exec_module(student_module)

                student_func = getattr(student_module, result.function_name)
                _ = student_func(
                    *result.input
                )  # We don't care about the output as we have already marked it.

                # Show the students their plots so they can debug.
                plt.show()
