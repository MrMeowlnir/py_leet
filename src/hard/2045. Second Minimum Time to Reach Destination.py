from collections import deque
from src.tests import *
from src.bcolor import bcolors
from typing import List


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        """
        A city is represented as a bi-directional connected graph with n vertices
        where each vertex is labeled from 1 to n (inclusive).
        The edges in the graph are represented as a 2D integer array edges,
        where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi.
        Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.
        The time taken to traverse any edge is time minutes.

        Each vertex has a traffic signal which changes its color from green to red and vice versa every change minutes.
        All signals change at the same time. You can enter a vertex at any time,
        but can leave a vertex only when the signal is green. You cannot wait at a vertex if the signal is green.

        The second minimum value is defined as the smallest value strictly larger than the minimum value.

        For example the second minimum value of [2, 3, 4] is 3, and the second minimum value of [2, 2, 4] is 4.
        Given n, edges, time, and change, return the second minimum time it will take to go from vertex 1 to vertex n.
        """
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        q = deque([(1, 1)])
        dist1 = [-1] * (n + 1)
        dist2 = [-1] * (n + 1)
        dist1[1] = 0
        while q:
            x, freq = q.popleft()
            t = dist1[x] if freq == 1 else dist2[x]
            if (t // change) % 2:
                t = change * (t // change + 1) + time
            else:
                t += time
            for y in g[x]:
                if dist1[y] == -1:
                    dist1[y] = t
                    q.append((y, 1))
                elif dist2[y] == -1 and dist1[y] != t:
                    if y == n:
                        return t
                    dist2[y] = t
                    q.append((y, 2))
        return 0


if __name__ == '__main__':
    solution = Solution()
    func_test = solution.secondMinimum
    cases = [
        {'data':
            {
                'n': 5,
                'edges': [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]],
                'time': 3,
                'change': 5,
            },
            'result': 13},
        {'data':
            {
                'n': 2,
                'edges': [[1, 2]],
                'time': 3,
                'change': 2,
            },
            'result': 11},
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
