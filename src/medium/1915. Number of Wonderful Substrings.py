from src.tests import *
from src.bcolor import bcolors
from typing import Optional, Any

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        """
        A wonderful string is a string where at most one letter appears an odd number of times.

        For example, "ccjjc" and "abab" are wonderful, but "ab" is not.
        Given a string word that consists of the first ten lowercase English letters ('a' through 'j'),
        return the number of wonderful non-empty substrings in word.
        If the same substring appears multiple times in word, then count each occurrence separately.

        A substring is a contiguous sequence of characters in a string.
        """
        counts = [0] * 1024
        counts[0] = 1
        wonderfulCount = 0
        mask = 0

        for c in word:
            mask ^= 1 << (ord(c) - ord('a'))
            counts[mask] += 1

        for msk in range(1024):
            if counts[msk] != 0:
                cntAtMsk = counts[msk]
                wonderfulCount += ((cntAtMsk - 1) * cntAtMsk) >> 1
                bit = 1
                while bit <= msk:
                    if (msk & bit) != 0:
                        wonderfulCount += counts[msk ^ bit]
                    bit <<= 1

        return wonderfulCount


if __name__ == '__main__':
    solution = Solution()
    func_test = solution.wonderfulSubstrings
    cases = [
        {'data':
            {
                'word': 'aba'
            },
            'result': 4},
        {'data':
            {
                'word': 'aabb',
            },
            'result': 9},
        {'data':
            {
                'word': 'he',
            },
            'result': 2},
    ]
    failed = []
    for case in cases:
        fail = print_tests(func_test, case['data'], case['result'])
        if fail:
            failed.append(fail)

    if failed:
        print(f'{bcolors.WARNING}Total failed {len(failed)} of test cases{bcolors.ENDC}')
    for fail in failed:
        print(f'{fail["Case"]}: '
              f'Expected: {bcolors.OKGREEN}{fail["Expected"]}{bcolors.ENDC}, '
              f'Actual: {bcolors.FAIL}{fail["Actual"]}{bcolors.ENDC}')
