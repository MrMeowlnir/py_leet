from typing import Optional, Any, Callable
from src.bcolor import bcolors


def counter(func):
    def wrapper(*args):
        wrapper.count += 1
        print(f'{bcolors.OKCYAN}Test #{wrapper.count}:{bcolors.ENDC}')
        print(f'Case: {args[1]}')
        print(f'Expected: {args[2]}')
        return func(*args)

    wrapper.count = 0
    return wrapper


@counter
def print_tests(func: Callable,
                data: dict,
                expected: Any,
                failed: Optional[list[dict]] = None) -> None:
    if not failed:
        failed = []
    actual_result = func(**data)
    print(f'Actual result: {actual_result}')
    if actual_result != expected:
        print(f'{bcolors.FAIL}================= Failed! ================={bcolors.ENDC}')
        failed.append(
            {'Case': data,
             'Expected result': expected,
             'Actual result': actual_result})
    else:
        print(f'{bcolors.OKGREEN}================= Passed ================={bcolors.ENDC}')


