from typing import Any, Callable
from src.bcolor import bcolors


def counter_failer(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f'{bcolors.OKCYAN}Test #{wrapper.count}:{bcolors.ENDC}')
        print(f'Case: {kwargs['data']}')
        print(f'Expected: {kwargs['expected']}')
        expected, actual_result = func(*args)
        print(f'Actual result: {actual_result}')
        if not expected:
            print(f'{bcolors.FAIL}Failed!{bcolors.ENDC}')
            wrapper.failed.append(
                {'#': wrapper.count,
                 'Case': kwargs['data'],
                 'Expected result': kwargs['expected'],
                 'Actual result': actual_result})
        else:
            print(f'{bcolors.OKGREEN}Passed{bcolors.ENDC}')
        print('=' * 52)

    wrapper.count = 0
    wrapper.failed = []
    return wrapper


@counter_failer
def test_prints(func: Callable,
                data: dict,
                expected: Any) -> (bool, Any):
    actual_result = func(**data)
    return actual_result == expected, actual_result


if test_prints.failed:
    print(f'{bcolors.WARNING}Total failed {len(test_prints.failed)} cases{bcolors.ENDC}')
for fail in test_prints.failed:
    print(f'{fail}')
