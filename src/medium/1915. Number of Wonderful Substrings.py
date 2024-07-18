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
        count = [0] * 1024
        mask = 0
        count[0] = 1
        result = 0
        for c in word:
            mask ^= 1 << (ord(c) - ord('a'))
            result += count[mask]
            for i in range(10):
                result += count[mask ^ (1 << i)]
            count[mask] += 1
        return result


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
