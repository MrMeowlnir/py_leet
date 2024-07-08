from typing import Optional


class Solution:
    def findTheWinner(self, n: int, k: int) -> Optional[int]:
        if n == 0:
            return None
        if n == 1:
            return 1

        lst = [i+1 for i in range(n)]
        cur_pos = 0
        while len(lst) > 1:
            cur_pos = (k+cur_pos - 1) % len(lst)
            lst.remove(lst[cur_pos])
        return lst[0]

    def recursiveFindTheWinner(self, n: int, k: int) -> Optional[int]:
        if n == 0:
            return None
        if n == 1:
            return 1

        return (self.recursiveFindTheWinner(n-1, k) + k - 1) % n + 1


if __name__ == '__main__':
    solution = Solution()
    cases = [dict({'n': 5,
                   'k': 2}),
             dict({'n': 6,
                   'k': 5}),
             ]
    for case in cases:
        print(solution.findTheWinner(**case), solution.recursiveFindTheWinner(**case))
