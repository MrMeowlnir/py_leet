import heapq

class Solution:
    def mincostToHireWorkers(self, quality: list[int], wage: list[int], k: int) -> float:
        result = float('inf')
        stats = []
        for i in range(len(quality)):
            stats.append((wage[i]/quality[i], quality[i]))
        stats.sort(key=lambda x: x[0])

        maxHeap = []
        total_quality = 0
        for rate, quality in stats:
            heapq.heappush(maxHeap, -quality)
            total_quality += quality
            if len(maxHeap) > k:
                total_quality += heapq.heappop(maxHeap)
            if len(maxHeap) == k:
                result = min(result, rate * total_quality)

        return result


if __name__ == '__main__':
    solution = Solution()
    cases = [dict({'quality': [10, 20, 5],
                   'wage': [70, 50, 30],
                   'k': 2}),
             dict({'quality': [3, 1, 10, 10, 1],
                   'wage': [4, 8, 2, 2, 7],
                   'k': 3}),
             ]
    for case in cases:
        print(solution.mincostToHireWorkers(**case))
