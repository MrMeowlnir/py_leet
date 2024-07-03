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

        return min(nums[-4]-nums[0],
                   nums[-3]-nums[1],
                   nums[-2]-nums[2],
                   nums[-1]-nums[3])


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
