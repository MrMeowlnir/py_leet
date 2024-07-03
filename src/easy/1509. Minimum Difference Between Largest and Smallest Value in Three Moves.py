from statistics import median


class Solution(object):
    def minDifference(self, nums: list[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
         """

        if len(nums) <= 4:
            return 0

        nums.sort()

        return min(max(nums[:-3])-min(nums[:-3]),
                   max(nums[1:-2])-min(nums[1:-2]),
                   max(nums[2:-1])-min(nums[2:-1]),
                   max(nums[3:])-min(nums[3:]))


if __name__ == "__main__":
    solution = Solution()
    cases = [
        [5, 3, 2, 4],
        [1, 5, 0, 14, 15],
        [3, 100, 20],
        [82, 81, 95, 75, 20]
    ]

    for case in cases:
        print(solution.minDifference(case))
