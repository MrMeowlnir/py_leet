from src.tests import *
from src.bcolor import bcolors
from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        """
        Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

        A lucky number is an element of the matrix such
        that it is the minimum element in its row and maximum in its column.
        """
        if not matrix:
            return []
        result = []
        for i in range(len(matrix)):
            minIdx = matrix[i].index(min(matrix[i]))
            column = [x[minIdx] for x in matrix]
            maxIdx = column.index(max(column))
            if i == maxIdx:
                result.append(matrix[i][minIdx])

        return result


if __name__ == '__main__':
    solution = Solution()
    func_test = solution.luckyNumbers
    cases = [
        {'data':
            {
                'matrix': [[3, 7, 8], [9, 11, 13], [15, 16, 17]],
            },
            'result': [15]},
        {'data':
            {
                'matrix': [[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]],
            },
            'result': [12]},
        {'data':
            {
                'matrix': [[7, 8], [1, 2]],
            },
            'result': [7]},
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
