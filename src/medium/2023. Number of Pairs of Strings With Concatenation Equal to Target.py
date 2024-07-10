from src.tests import *


class Solution:
    def numOfPairs(self, nums: list[str], target: str) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and (nums[i] + nums[j]) == target:
                    count += 1
        return count


if __name__ == '__main__':
    solution = Solution()
    func_test = solution.numOfPairs
    cases = [
        {'data':
            {
                'nums': ["777", "7", "77", "77"],
                'target': "7777"
            },
            'result': 4},
        {'data':
            {
                'nums': ["123", "4", "12", "34"],
                'target': "1234"
            },
            'result': 2},
        {'data':
            {
                'nums': ["1", "1", "1"],
                'target': "11",
            },
            'result': 6}
    ]

    for case in cases:
        test_prints(func_test, case['data'], case['result'])

