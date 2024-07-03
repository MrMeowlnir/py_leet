class Solution(object):
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        for i in range(len(tickets)):
            if tickets[i]>tickets[k]:
                tickets[i]=tickets[k]
                if i>k:
                    count+=1
        return sum(tickets)-count


if __name__ == "__main__":
    solution = Solution()
    cases = [
        ([2, 3, 2], 2),
        ([5, 1, 1, 1], 0),
        ([84, 49, 5, 24, 70, 77, 87, 8], 3)
    ]

    for case in cases:
        print(solution.timeRequiredToBuy(*case))
