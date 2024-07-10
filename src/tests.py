from typing import Optional, Any, Callable
from src.bcolor import bcolors


def test_prints(func: Callable,
                data: dict,
                expected: Any,
                count: int = 0,
                failed: Optional[list] = None) -> None:
    if failed is None:
        failed = []
    print(f'{bcolors.OKCYAN}Test #{count}:{bcolors.ENDC}')
    print(f'Case: {data}')
    print(f'Expected: {expected}')
    actual_result = func(**data)
    print(f'Actual result: {actual_result}')
    if actual_result != expected:
        print(f'{bcolors.FAIL}Failed!{bcolors.ENDC}')
        failed.append({'#': count, 'Case': data, 'Expected result': expected, 'Actual result': actual_result})
    else:
        print(f'{bcolors.OKGREEN}Passed{bcolors.ENDC}')
    print('=' * 52)
