class Solution(object):
    def reversePrefix(self, word: str, ch: str) -> str:
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        idx = word.find(ch)
        if idx == -1:
            return word
        return word[:word.find(ch) + 1][::-1] + word[word.find(ch) + 1:]


if __name__ == "__main__":
    solution = Solution()
    cases = [
        ('abcdefd', 'd'),
        ('xyxzxe', 'z'),
        ('abcd', 'z'),
    ]

    for case in cases:
        print(solution.reversePrefix(*case))