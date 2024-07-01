class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        return min({
                    'b': text.count('b'),
                    'a': text.count('a'),
                    'l': text.count('l') // 2,
                    'o': text.count('o') // 2,
                    'n': text.count('n')
                   }.values())


if __name__ == '__main__':
    solution = Solution()
    cases = ['nlaebolko',
             'loonbalxballpoon',
             'leetcode']
    for case in cases:
        print(solution.maxNumberOfBalloons(case))
