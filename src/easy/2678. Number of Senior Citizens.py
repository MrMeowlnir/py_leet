from src.tests import *
from src.bcolor import bcolors
from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        """
        You are given a 0-indexed array of strings details.
        Each element of details provides information about a given passenger
        compressed into a string of length 15. The system is such that:

        The first ten characters consist of the phone number of passengers.
        The next character denotes the gender of the person.
        The following two characters are used to indicate the age of the person.
        The last two characters determine the seat allotted to that person.

        Return the number of passengers who are strictly more than 60 years old.
        """
        return sum(1 if int(s[11:13])>60 else 0 for s in details)


if __name__ == '__main__':
    solution = Solution()
    func_test = solution.countSeniors
    cases = [
        {'data':
            {
                'details': ["7868190130M7522","5303914400F9211","9273338290F4010"]
            },
            'result': 2},
        {'data':
            {
                'details': ["1313579440F2036","2921522980M5644"]
            },
            'result': 0},
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
