from collections import defaultdict
from src.tests import *
from src.bcolor import bcolors
from typing import List


class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
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
        def dfs(src: int, graph: defaultdict, visited: set[int], cur_path: set[int], res: List[int]) -> bool:
            if src in cur_path:
                return False
            if src in visited:
                return True

            visited.add(src)
            cur_path.add(src)

            for neighbour in graph[src]:
                if not dfs(neighbour, graph, visited, cur_path, res):
                    return False

            cur_path.remove(src)
            res.append(src)
            return True

        def order(conditions: List[List[int]]) -> List[int]:
            graph = defaultdict(list)
            for src, dst in conditions:
                graph[dst].append(src)
            visited: set[int] = set()
            cur_path: set[int] = set()
            res: List[int] = []
            for src in range(1, k + 1):
                if not dfs(src, graph, visited, cur_path, res):
                    return []
            return res

        updown_order: List[int] = order(rowConditions)
        leftright_order: List[int] = order(colConditions)
        if [] in (updown_order, leftright_order):
            return []

        val_pos: dict[int, List[int]] = {
            n: [0, 0] for n in range(1, k + 1)
        }
        for idx, val in enumerate(updown_order):
            val_pos[val][0] = idx
        for idx, val in enumerate(leftright_order):
            val_pos[val][1] = idx

        matrix: List[List[int]] = [[0] * k for _ in range(k)]
        for value in range(1, k + 1):
            row, col = val_pos[value]
            matrix[row][col] = value

        return matrix


if __name__ == '__main__':
    solution = Solution()
    func_test = solution.buildMatrix
    cases = [
        {'data':
            {
                'k': 3,
                'rowConditions': [[1, 2], [3, 2]],
                'colConditions': [[2, 1], [3, 2]],
            },
            'result': [[0, 0, 1], [3, 0, 0], [0, 2, 0]]},
        {'data':
            {
                'k': 3,
                'rowConditions': [[1, 2], [2, 3], [3, 1], [2, 3]],
                'colConditions': [[2, 1]],
            },
            'result': []},
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
