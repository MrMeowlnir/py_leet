class Solution(object):
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        """
        :type arr: List[int]
        :rtype: bool
        """
        counter = 0
        for num in arr:
            if num % 2 == 1:
                counter += 1
                if counter == 3:
                    return True
            else:
                counter = 0
        return False


if __name__ == '__main__':
    solution = Solution()
    arr1 = [2, 6, 4, 1]
    arr2 = [1, 2, 34, 3, 4, 5, 7, 23, 12]

    print(solution.threeConsecutiveOdds(arr1))
    """ False """

    print(solution.threeConsecutiveOdds(arr2))
    """ True ([5, 7, 23]) """
