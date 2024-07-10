from src.tests import *
from src.bcolor import bcolors


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
    print(type(func_test))
    cases = [
        {'data':
            {
                'nums': ["777", "7", "77", "77"],
                'target': "7777"
            },
            'result': 1},
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
    case_count = 0
    failed = []
    for case in cases:
        case_count += 1
        test_prints(func_test, case['data'], case['result'], case_count, failed)
    if failed:
        print(f'{bcolors.WARNING}Total failed {len(failed)} cases{bcolors.ENDC}')
    for fail in failed:
        print(f'{fail}')
