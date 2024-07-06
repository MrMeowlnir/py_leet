class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        ptr = 1
        dp = 1
        for _ in range(time):
            if ptr+dp > n or ptr+dp < 1:
                dp *= -1
            ptr += dp
        return ptr


if __name__ == '__main__':
    solution = Solution()
    cases = [dict({'n': 4,
                   'time': 5}),
             dict({'n': 4,
                   'time': 5}),
             ]
    for case in cases:
        print(solution.passThePillow(**case))
