from src.tests import *
from src.bcolor import bcolors

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n << 1 if n & 1 else n


if __name__ == '__main__':
    solution = Solution()
    func_test = solution.smallestEvenMultiple
    cases = [
        {'data':
            {
                'n': 5,
            },
            'result': 10},
        {'data':
            {
                'n': 6,
            },
            'result': 6}
    ]
    failed = []
    for case in cases:
        fail = print_tests(func_test, case['data'], case['result'])
        if fail:
            failed.append(fail)

    if failed:
        print(f'{bcolors.WARNING}Total failed {len(failed)} of test cases{bcolors.ENDC}')
    for fail in failed:
        print(f'{fail["Case"]}: '
              f'Expected: {bcolors.OKGREEN}{fail["Expected"]}{bcolors.ENDC}, '
              f'Actual: {bcolors.FAIL}{fail["Actual"]}{bcolors.ENDC}')
