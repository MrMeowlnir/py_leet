class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        if customers == [[]]:
            return 0
        wt = []
        finish = 0
        for customer in customers:
            start = max(customer[0], finish)
            finish = start + customer[1]
            wt.append(finish - customer[0])
        return sum(wt) / len(wt)

    def fasterAverageWaitingTime(self, customers: list[list[int]]) -> float:
        n = len(customers)
        wait_sum = 0
        finish = 0
        for customer in customers:
            coming, time = customer[0], customer[1]
            if coming < finish:
                wait_sum += finish - coming + time
                finish += time
            else:
                wait_sum += time
                finish = coming + time
        return wait_sum / n


if __name__ == '__main__':
    solution = Solution()
    cases = [dict({'customers': [[1, 2], [2, 5], [4, 3]]}),
             dict({'customers': [[5, 2], [5, 4], [10, 3], [20, 1]]}),
             ]
    for case in cases:
        print(solution.fasterAverageWaitingTime(**case))
