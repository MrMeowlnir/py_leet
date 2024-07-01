class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n % 2 == 0:
            return 'a' * (n - 1) + 'b'
        return 'a' * n


if __name__ == '__main__':
    solution = Solution()
    cases = [4,
             2,
             7,
             ]
    for case in cases:
        print(solution.generateTheString(case))
