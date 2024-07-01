class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        distances = {}
        for point in points:
            if (x == point[0] or y == point[1]) and not (abs(x - point[0]) + abs(y - point[1]) in distances.keys()):
                distances[abs(x - point[0]) + abs(y - point[1])] = point
        if not distances:
            return -1
        return points.index(distances[min(distances.keys())])


if __name__ == '__main__':
    solution = Solution()
    cases = [(3, 4, [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]),
             (3, 4, [[3, 4]]),
             (3, 4, [[2, 3]])]
    for case in cases:
        print(solution.nearestValidPoint(*case))
