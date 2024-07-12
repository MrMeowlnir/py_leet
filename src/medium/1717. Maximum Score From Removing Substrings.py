from src.tests import *
from src.bcolor import bcolors


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        """
        You are given a string s and two integers x and y. You can perform two types of operations any number of times.

        Remove substring "ab" and gain x points.
        For example, when removing "ab" from "cabxbae" it becomes "cxbae".
        Remove substring "ba" and gain y points.
        For example, when removing "ba" from "cabxbae" it becomes "cabxe".
        Return the maximum points you can gain after applying the above operations on s.
        """
        big = x if x > y else y
        small = y if x > y else x
        first = 'a' if x > y else 'b'
        second = 'b' if x > y else 'a'
        points = 0
        stack1, stack2 = [], []
        for ch in s:
            if ch == second and stack1 and stack1[-1] == first:
                points += big
                stack1.pop()
            else:
                stack1.append(ch)
        while stack1:
            ch = stack1.pop()
            if ch == second and stack2 and stack2[-1] == first:
                points += small
                stack2.pop()
            else:
                stack2.append(ch)

        return points


if __name__ == '__main__':
    solution = Solution()
    func_test = solution.maximumGain
    cases = [
        {'data':
            {
                's': 'cdbcbbaaabab',
                'x': 4,
                'y': 5,
            },
            'result': 19},
        {'data':
            {
                's': 'aabbaaxybbaabb',
                'x': 5,
                'y': 4,
            },
            'result': 20},
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
