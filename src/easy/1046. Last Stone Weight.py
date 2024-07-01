class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        if len(stones) == 0:
            return 0
        if len(stones) == 1:
            return stones[0]
        y = max(stones)
        stones.remove(max(stones))
        x = max(stones)
        stones.remove(max(stones))
        if x != y:
            stones.append(y - x)
        return self.lastStoneWeight(stones)


if __name__ == '__main__':
    solution = Solution()
    cases = [[2, 7, 4, 1, 8, 1],
             [1],
             ]
    for case in cases:
        print(solution.lastStoneWeight(case))
