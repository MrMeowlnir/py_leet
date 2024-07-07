class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        full_bottles = numBottles
        empty_bottles = 0
        drinked_bottles = 0
        while full_bottles + empty_bottles >= numExchange:
            drinked_bottles += full_bottles
            full_bottles, empty_bottles = ((full_bottles + empty_bottles)//numExchange,
                                           (full_bottles + empty_bottles) % numExchange)
        return drinked_bottles + full_bottles

    def recursive_numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        def exchange(n, k):
            if n < k:
                return 0
            n0, r = divmod(n, k)
            return n0 + exchange(n0+r, k)

        return numBottles + exchange(numBottles, numExchange)


if __name__ == '__main__':
    solution = Solution()
    cases = [dict({'numBottles': 15,
                   'numExchange': 8}),
             dict({'numBottles': 9,
                   'numExchange': 3}),
             dict({'numBottles': 15,
                   'numExchange': 4}),
             ]
    for case in cases:
        print(solution.recursive_numWaterBottles(**case))
