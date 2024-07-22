from collections import defaultdict
from src.tests import *
from src.bcolor import bcolors
from typing import List, Tuple


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        """
        You are given an array of strings names, and an array heights that consists of distinct positive integers.
        Both arrays are of length n.

        For each index i, names[i] and heights[i] denote the name and height of the ith person.

        Return names sorted in descending order by the people's heights.
        """
        # Combine names and heights into a list of tuples
        people: List[Tuple[str, int]] = list(zip(names, heights))

        # Sort the list of tuples in descending order by height
        people.sort(key=lambda x: x[1], reverse=True)

        # Extract the names from the sorted list of tuples
        sorted_names = [person[0] for person in people]

        return sorted_names


if __name__ == '__main__':
    solution = Solution()
    func_test = solution.sortPeople
    cases = [
        {'data':
            {
                'names': ["Mary", "John", "Emma"],
                'heights': [180, 165, 170],
            },
            'result': ["Mary", "Emma", "John"]},
        {'data':
            {
                'names': ["Alice", "Bob", "Bob"],
                'heights': [155, 185, 150],
            },
            'result': ["Bob", "Alice", "Bob"]},
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
