from typing import Callable, Tuple, TypeVar


T = TypeVar("T")


def run_tests(tests: Tuple[str, T], func: Callable[[str], T]):
    for idx, (test_string, answer) in enumerate(tests):
        result = func(test_string)
        if result != answer:
            print(f"[*] TEST #{idx} FAILED: expected {answer}, but got {result}")
            print("\t", test_string)
            continue
        print(f"Test #{idx} passed")
        print("\t", test_string)
        print("\t", result)
