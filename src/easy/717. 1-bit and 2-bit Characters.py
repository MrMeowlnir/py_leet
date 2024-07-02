class Solution(object):
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        """
        :type bits: List[int]
        :rtype: bool
        """
        pointer = 0
        while pointer < len(bits)-2:
            pointer += 1 + bits[pointer]

        return not bool(bits[pointer])


if __name__ == '__main__':
    solution = Solution()
    cases = [[1, 1, 0, 0],
             [1, 1, 0],
             [1, 1, 1, 0],
             [0, 1, 0],
             [1, 0, 0, 1, 0]]
    for case in cases:
        print(solution.isOneBitCharacter(case))
