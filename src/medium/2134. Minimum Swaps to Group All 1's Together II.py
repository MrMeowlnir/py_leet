from src.tests import *
from src.bcolor import bcolors
from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        """
        A swap is defined as taking two distinct positions in an array and swapping the values in them.

        A circular array is defined as an array where we consider the first element and the last element to be adjacent.

        Given a binary circular array nums, return the minimum number of swaps required to group all 1's present
        in the array together at any location.
        """
        n = len(nums)
        ones = sum(nums)
        if ones == 0 or ones == n:
            return 0
        curr = sum(nums[:ones])
        maxi = curr
        for i in range(n):
            curr -= nums[i]
            curr += nums[(i + ones) % n]
            maxi = max(maxi, curr)
        return ones - maxi


if __name__ == '__main__':
    solution = Solution()
    func_test = solution.minSwaps
    cases = [
        {'data':
            {
                'nums': [0, 1, 0, 1, 1, 0, 0]
            },
            'result': 1},
        {'data':
            {
                'nums': [0, 1, 1, 1, 0, 0, 1, 1, 0]
            },
            'result': 2},
        {'data':
            {
                'nums': [1, 1, 0, 0, 1]
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
