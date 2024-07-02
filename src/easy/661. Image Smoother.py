class Solution(object):
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(img)
        m = len(img[0])
        answer = [[0]*m for _ in range(n)]
        for r, row in enumerate(img):
            for c, col in enumerate(row):
                s = 0
                count = 0
                for dx in range(-1,2):
                    for dy in range(-1,2):
                        if 0 <= r+dx < n and 0 <= c+dy < m:
                            s += img[r+dx][c+dy]
                            count += 1
                answer[r][c] = s // count
        return answer


if __name__ == "__main__":
    solution = Solution()
    cases = [
        [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
        [[100, 200, 100], [200, 50, 200], [100, 200, 100]]
    ]

    for case in cases:
        print(solution.imageSmoother(case))
