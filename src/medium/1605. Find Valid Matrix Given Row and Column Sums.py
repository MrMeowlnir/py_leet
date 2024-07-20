from src.tests import *
from src.bcolor import bcolors
from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        """
        You are given two arrays rowSum and colSum of non-negative integers
        where rowSum[i] is the sum of the elements in the ith row and
        colSum[j] is the sum of the elements of the jth column of a 2D matrix.
        In other words, you do not know the elements of the matrix, but you do know the sums of each row and column.

        Find any matrix of non-negative integers of size rowSum.length x colSum.length
        that satisfies the rowSum and colSum requirements.

        Return a 2D array representing any matrix that fulfills the requirements.
        It's guaranteed that at least one matrix that fulfills the requirements exists.
        """
        numRows, numCols = len(rowSum), len(colSum)
        res = [[0 for _ in range(numCols)] for _ in range(numRows)]
        for i in range(numRows):
            j = 0
            while j < numCols and rowSum[i] > 0:
                res[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= res[i][j]
                colSum[j] -= res[i][j]
                j += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    func_test = solution.restoreMatrix
    cases = [
        {'data':
            {
                'rowSum': [3, 8],
                'colSum': [4, 7],
            },
            'result': [[3, 0], [1, 7]]},
        {'data':
            {
                'rowSum': [5, 7, 10],
                'colSum': [8, 6, 8],
            },
            'result': [[5, 0, 0], [3, 4, 0], [0, 2, 8]]},
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
