class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        res_arr = []
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                res_arr.append([arr[i], arr[j], arr[i]/arr[j]])
        res_arr.sort(key=lambda x: x[2])
        return [res_arr[k-1][0], res_arr[k-1][1]]


if __name__ == '__main__':
    solution = Solution()
    cases = [dict({'arr': [1, 2, 3, 5],
                   'k': 3}),
             dict({'arr': [1, 7],
                   'k': 1}),
             ]
    for case in cases:
        print(solution.kthSmallestPrimeFraction(**case))
