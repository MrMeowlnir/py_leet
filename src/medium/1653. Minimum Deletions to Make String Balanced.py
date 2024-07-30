from collections import deque
from src.tests import *
from src.bcolor import bcolors
from typing import List


class Solution:
    def minimumDeletions(self, s: str) -> int:
        """
        You are given a string s consisting only of characters 'a' and 'b'​​​​.

        You can delete any number of characters in s to make s balanced.
        s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

        Return the minimum number of deletions needed to make s balanced.
        """
        bCount = 0
        minDeletions = 0
        for char in s:
            if char == 'a':
                minDeletions = min(minDeletions + 1, bCount)
            else:
                bCount += 1
        return minDeletions


if __name__ == '__main__':
    solution = Solution()
    func_test = solution.minimumDeletions
    cases = [
        {'data':
            {
                's': 'aababbab',
            },
            'result': 2},
        {'data':
            {
                's': 'bbaaaaabb',
            },
            'result': 2},
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
