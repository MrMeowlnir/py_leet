class Solution:
    def reverseString(self, s: list[str]) -> list[str]:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n // 2):
            s[i], s[n-1-i] = s[n-1-i], s[i]
        return s


if __name__ == '__main__':
    solution = Solution()
    cases = [dict({'s': ['h', 'e', 'l', 'l', 'o']}),
             dict({'s': ['H', 'a', 'n', 'n', 'a', 'h']}),
             ]
    for case in cases:
        print(solution.reverseString(**case))
