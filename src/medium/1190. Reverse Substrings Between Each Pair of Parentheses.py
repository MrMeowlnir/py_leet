from src.tests import *
from src.bcolor import bcolors


class Solution:
    def reverseParentheses(self, s: str) -> str:
        def reverse_inner(s: str) -> str:
            last_open = -1
            first_close = s.index(')')
            for i in range(len(s[:first_close])):
                if s[i] == '(':
                    last_open = i

            res = s[:last_open] + s[last_open + 1:first_close][::-1]
            if first_close != len(s):
                res += s[first_close + 1:]
            print(res)
            return res
        while s.count('(') != 0:
            s = reverse_inner(s)

        return s


if __name__ == '__main__':
    solution = Solution()
    func_test = solution.reverseParentheses
    cases = [
        {'data':
            {
                's': '(abcd)'
            },
            'result': 'dcba'},
        {'data':
            {
                's': '(u(love)i)'
            },
            'result': 'iloveu'},
        {'data':
            {
                's': '(ed(et(oc))el)',
            },
            'result': 'leetcode'}
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
