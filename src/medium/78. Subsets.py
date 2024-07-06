class Solution:
    def subsets_slow(self, nums: list[int]) -> list[list[int]]:
        def dfs(i):
            if i == len(nums):
                result.append(t[:])
                return
            dfs(i+1)
            t.append(nums[i])
            dfs(i+1)
            t.pop()

        result = []
        t = []
        dfs(0)

        return result

    def subsets_fast(self, nums: list[int]) -> list[list[int]]:
        def backtrack(start: int, cur_subsets: list[int]):
            result.append(cur_subsets[:])
            for i in range(start, len(nums)):
                cur_subsets.append(nums[i])
                backtrack(i+1, cur_subsets)
                cur_subsets.pop()

        result = []
        backtrack(0, [])
        return result


if __name__ == '__main__':
    solution = Solution()
    cases = [dict({'nums': [1, 2, 3]}),
             dict({'nums': [0]}),
             ]
    for case in cases:
        print(solution.subsets_fast(**case))
