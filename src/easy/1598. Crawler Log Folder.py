from src.tests import *
from src.bcolor import bcolors

class Solution:
    def minOperations(self, logs: list[str]) -> int:
        res = 0
        for log in logs:
            if log == "../":
                res = max(0, res - 1)
            elif log == "./":
                continue
            else:
                res += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    func_test = solution.minOperations
    cases = [
        {'data':
            {
                'logs': ["d1/", "d2/", "../", "d21/", "./"],
            },
            'result': 2},
        {'data':
            {
                'logs': ["d1/", "d2/", "./", "d3/", "../", "d31/"],
            },
            'result': 3},
        {'data':
            {
                'logs': ["d1/", "../", "../", "../"],
            },
            'result': 0}
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
