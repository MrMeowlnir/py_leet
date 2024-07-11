from src.tests import *
from src.bcolor import bcolors


class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word

        return ''


if __name__ == '__main__':
    solution = Solution()
    func_test = solution.firstPalindrome
    cases = [
        {'data':
            {
                'words': ["abc", "car", "ada", "racecar", "cool"]
            },
            'result': 'ada'},
        {'data':
            {
                'words': ["notapalindrome", "racecar"]
            },
            'result': 'racecar'},
        {'data':
            {
                'words': ["def", "ghi"]
            },
            'result': ''}
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
