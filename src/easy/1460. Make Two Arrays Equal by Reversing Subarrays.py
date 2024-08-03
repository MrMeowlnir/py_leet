from src.tests import *
from src.bcolor import bcolors
from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        """
        You are given two integer arrays of equal length target and arr. In one step,
        you can select any non-empty subarray of arr and reverse it. You are allowed to make any number of steps.

        Return true if you can make arr equal to target or false otherwise.
        """
        return sorted(target) == sorted(arr)


if __name__ == '__main__':
    solution = Solution()
    func_test = solution.canBeEqual
    cases = [
        {'data':
            {
                'target': [1, 2, 3, 4],
                'arr': [2, 4, 1, 3]
            },
            'result': True},
        {'data':
            {
                'target': [7],
                'arr': [7]
            },
            'result': True},
        {'data':
            {
                'target': [3, 7, 9],
                'arr': [3, 7, 11]
            },
            'result': False},
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
