class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


if __name__ == '__main__':
    solution = Solution()
    cases = [dict({'nums': [2, 7, 11, 15],
                   'target': 9}),
             dict({'nums': [3, 2, 4],
                   'target': 6}),
             dict({'nums': [3, 3],
                   'target': 6}),
             ]
    for case in cases:
        print(solution.twoSum(**case))
