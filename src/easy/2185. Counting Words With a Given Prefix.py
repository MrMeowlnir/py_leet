from src.tests import *
from src.bcolor import bcolors


class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        count = 0
        for word in words:
            if word.startswith(pref):
                count += 1
        return count


if __name__ == '__main__':
    solution = Solution()
    func_test = solution.prefixCount
    cases = [
        {'data':
            {
                'words': ['pay', 'attention', 'practice', 'attend'],
                'pref': 'at',
            },
            'result': 2},
        {'data':
            {
                'words': ["leetcode", "win", "loops", "success"],
                'pref': 'code',
            },
            'result': 0},
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
