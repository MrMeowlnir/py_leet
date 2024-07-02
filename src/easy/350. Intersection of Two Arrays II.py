class Solution(object):
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []

        for num in set(nums2):
            res = res + [num] * min(nums1.count(num), nums2.count(num))

        return res


if __name__ == '__main__':
    solution = Solution()
    cases = [([1, 2, 2, 1], [2, 2]),
             ([4, 9, 5], [9, 4, 9, 8, 4]),
             ]
    for case in cases:
        print(solution.intersect(*case))
