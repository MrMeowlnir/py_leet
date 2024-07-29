from collections import deque
from src.tests import *
from src.bcolor import bcolors
from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        """
        There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

        You have to form a team of 3 soldiers amongst them under the following rules:

        Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
        A team is valid if: (rating[i] < rating[j] < rating[k])
        or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
        Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).
        """
        n = len(rating)
        count = 0

        for j in range(n):
            leftLess = leftGreater = rightLess = rightGreater = 0

            for i in range(j):
                if rating[i] < rating[j]:
                    leftLess += 1
                elif rating[i] > rating[j]:
                    leftGreater += 1

            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    rightLess += 1
                elif rating[k] > rating[j]:
                    rightGreater += 1

            count += leftLess * rightGreater + leftGreater * rightLess

        return count


if __name__ == '__main__':
    solution = Solution()
    func_test = solution.numTeams
    cases = [
        {'data':
            {
                'rating': [2, 5, 3, 4, 1],
            },
            'result': 3},
        {'data':
            {
                'rating': [2, 1, 3],
            },
            'result': 0},
        {'data':
            {
                'rating': [1, 2, 3, 4],
            },
            'result': 4},
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
