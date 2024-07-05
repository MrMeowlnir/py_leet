class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:  # slow version
        while min(students) < max(students):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                students.append(students.pop(0))
        while (len(students) > 0) and students[0] == sandwiches[0]:
            students.pop(0)
            sandwiches.pop(0)

        return len(students)

    def countStudents_fast(self, students: list[int], sandwiches: list[int]) -> int:  # fast version
        taste = {}
        count = len(students)
        for student in students:
            taste[student] = taste.get(student, 0) + 1
        for sandwich in sandwiches:
            if sandwich not in taste:
                return count

            if taste[sandwich] > 0:
                taste[sandwich] -= 1
                count -= 1
            else:
                return count

        return count


if __name__ == '__main__':
    solution = Solution()
    cases = [dict({'students': [1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                   'sandwiches': [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0]}),
             dict({'students': [1, 1, 0, 0],
                   'sandwiches': [0, 1, 0, 1]}),
             dict({'students': [1, 1, 1, 0, 0, 1],
                   'sandwiches': [1, 0, 0, 0, 1, 1]}),
             ]
    for case in cases:
        print(solution.countStudents_fast(**case))
