from collections import defaultdict
from src.tests import *
from src.bcolor import bcolors
from typing import List, Tuple


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        """
        You are given two 0-indexed strings source and target,
        both of length n and consisting of lowercase English letters.
        You are also given two 0-indexed character arrays original and changed,
        and an integer array cost, where cost[i] represents the cost of changing
        the character original[i] to the character changed[i].

        You start with the string source. In one operation,
        you can pick a character x from the string and change it to the character y at a cost of z
        if there exists any index j such that cost[j] == z, original[j] == x, and changed[j] == y.

        Return the minimum cost to convert the string source to the string target using any number of operations.
        If it is impossible to convert source to target, return -1.

        Note that there may exist indices i, j such that original[j] == original[i] and changed[j] == changed[i].
        """
        dp = [[float('inf')] * 26 for _ in range(26)]
        for i in range(26):
            dp[i][i] = 0
        for old, new, c in zip(original, changed, cost):
            old, new = ord(old) - ord('a'), ord(new) - ord('a')
            dp[old][new] = min(dp[old][new], c)
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    dp[i][k] = min(dp[i][k], dp[i][j] + dp[j][k])
        res = sum(dp[ord(s) - ord('a')][ord(t) - ord('a')] for s, t in zip(source, target))
        return res if res < float('inf') else -1


if __name__ == '__main__':
    solution = Solution()
    func_test = solution.minimumCost
    cases = [
        {'data':
            {
                'source': "abcd",
                'target': "acbe",
                'original': ["a", "b", "c", "c", "e", "d"],
                'changed': ["b", "c", "b", "e", "b", "e"],
                'cost': [2, 5, 5, 1, 2, 20],
            },
            'result': 28},
        {'data':
            {
                'source': "aaaa",
                'target': "bbbb",
                'original': ["a", "c"],
                'changed': ["c", "b"],
                'cost': [1, 2],
            },
            'result': 12},
        {'data':
            {
                'source': "abcd",
                'target': "abce",
                'original': ["a"],
                'changed': ["e"],
                'cost': [10000],
            },
            'result': -1},
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
