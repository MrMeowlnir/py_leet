import itertools
from functools import reduce


def subsets(nums: list[int]) -> list[list[int]]:
    result = [[]]
    for num in sorted(nums):
        result += [curr + [num] for curr in result]
    return result


def redc(func, iters: list[int]) -> int:
    if len(iters) == 0:
        return 0
    if len(iters) == 1:
        return iters[0]
    return reduce(func, iters)

class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        return sum(redc(lambda x, y: x ^ y, nums) for nums in subsets(nums))

    def recursiveSubsetXORSum(self, nums: list[int]) -> int:
        def dfs(i, total):
            if i == len(nums):
                return total
            return dfs(i + 1, total ^ nums[i]) + dfs(i + 1, total)
        return dfs(0, 0)

    def bitwiseSubsetXORSum(self, nums: list[int]) -> int:
        r = 0
        for num in nums:
            r |= num
        return r << len(nums) - 1


if __name__ == '__main__':
    solution = Solution()
    cases = [dict({'nums': [1, 3]}),
             dict({'nums': [5, 1, 6]}),
             dict({'nums': [3, 4, 5, 6, 7, 8]}),
             ]
    for case in cases:
        print(solution.bitwiseSubsetXORSum(**case))
