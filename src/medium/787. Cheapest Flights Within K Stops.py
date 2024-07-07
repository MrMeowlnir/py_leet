import heapq, collections, math


class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        min_cost = {src: 0}
        queue = collections.deque([(src, 0, k + 1)])

        while queue:
            u, cost, stops = queue.popleft()
            if u == dst:
                continue
            if stops > 0:
                for v, w in graph[u]:
                    if v not in min_cost or cost + w < min_cost[v]:
                        min_cost[v] = cost + w
                        queue.append((v, cost + w, stops - 1))

        return min_cost.get(dst, -1)


if __name__ == '__main__':
    solution = Solution()
    cases = [dict({'n': 4,
                   'flights': [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
                   'src': 0,
                   'dst': 3,
                   'k': 1}),
             dict({'n': 3,
                   'flights': [[0, 1, 100], [1, 2, 100], [0, 2, 500]],
                   'src': 0,
                   'dst': 2,
                   'k': 1}),
             dict({'n': 3,
                   'flights': [[0,1,100],[1,2,100],[0,2,500]],
                   'src': 0,
                   'dst': 2,
                   'k': 0}),
             ]
    for case in cases:
        print(solution.findCheapestPrice(**case))
