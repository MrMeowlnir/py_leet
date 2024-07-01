class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = {}
        for i in set(nums):
            if nums.count(i) in freq.keys():
                freq[nums.count(i)].append(i)
            else:
                freq[nums.count(i)] = [i]

        res = []
        for key in sorted(freq.keys()):
            res = res + sorted(freq[key] * key, reverse=True)

        return res


if __name__ == '__main__':
    solution = Solution()
    cases = [[1, 1, 2, 2, 2, 3],
             [2, 3, 1, 3, 2],
             [-1, 1, -6, 4, 5, -6, 1, 4, 1],
             ]
    for case in cases:
        print(solution.frequencySort(case))
