class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[1])
        arrows = 1
        end_point = points[0][1]
        for start, end in points:
            if start > end_point:
                arrows += 1
                end_point = end
        return arrows


if __name__ == '__main__':
    solution = Solution()
    cases = [dict({'points': [[10, 16], [2, 8], [1, 6], [7, 12]]}),
             dict({'points': [[1, 2], [3, 4], [5, 6], [7, 8]]}),
             dict({'points': [[1, 2], [2, 3], [3, 4], [4, 5]]}),
             ]
    for case in cases:
        print(solution.findMinArrowShots(**case))
