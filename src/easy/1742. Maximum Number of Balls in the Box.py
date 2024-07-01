class Solution(object):
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        boxes = [0] * 1000
        for num in range(lowLimit, highLimit + 1):
            boxes[sum([int(digit) for digit in str(num)])] += 1
        return max(boxes)


if __name__ == '__main__':
    solution = Solution()
    cases = [{'lowLimit': 1, 'highLimit': 10},
             {'lowLimit': 5, 'highLimit': 15},
             {'lowLimit': 19, 'highLimit': 28}]
    for case in cases:
        print(solution.countBalls(case['lowLimit'], case['highLimit']))
