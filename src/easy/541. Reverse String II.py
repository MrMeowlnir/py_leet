class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = ''
        while len(s) >= k:
            res += s[:k][::-1] + s[k:2*k]
            s = s[2 * k:]
        if len(s) > 0:
            res += s[::-1]

        return res


if __name__ == '__main__':
    solution = Solution()
    cases = [('abcdefg', 2),
             ('abcd', 2),
             ('hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl',
              39)]
    for case in cases:
        print(solution.reverseStr(*case))

