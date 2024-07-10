from src.tests import *
from src.bcolor import bcolors


class Solution:
    def largestInteger(self, num: int) -> int:
        digits = list(map(int, str(num)))
        evens = sorted(x for x in digits if not (x & 1))
        odds = sorted(x for x in digits if x & 1)
        return int(''.join(str(odds.pop() if x & 1 else evens.pop()) for x in digits))


if __name__ == '__main__':
    solution = Solution()
    func_test = solution.largestInteger
    cases = [
        {'data':
            {
                'num': 1234
            },
            'result': 3412},
        {'data':
            {
                'num': 65875,
            },
            'result': 87655},
        {'data':
            {
                'num': 247,
            },
            'result': 427},
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
