from src.tests import *
from src.bcolor import bcolors


class Solution:
    def survivedRobotsHealths(self, positions: list[int], healths: list[int], directions: str) -> list[int]:
        """
        There are n 1-indexed robots, each having a position on a line, health, and movement direction.

        You are given 0-indexed integer arrays positions, healths, and a string directions
        (directions[i] is either 'L' for left or 'R' for right). All integers in positions are unique.

        All robots start moving on the line simultaneously at the same speed in their given directions.
        If two robots ever share the same position while moving, they will collide.

        If two robots collide, the robot with lower health is removed from the line,
        and the health of the other robot decreases by one.
        The surviving robot continues in the same direction it was going.
        If both robots have the same health, they are both removed from the line.

        Your task is to determine the health of the robots that survive the collisions,
        in the same order that the robots were given, i.e. final heath of robot 1 (if survived),
        final health of robot 2 (if survived), and so on. If there are no survivors, return an empty array.

        Return an array containing the health of the remaining robots (in the order they were given in the input),
        after no further collisions can occur.

        Note: The positions may be unsorted.
        """
        hashmap = sorted([{'idx': i,
                           'position': positions[i],
                           'health': healths[i],
                           'direction': directions[i]} for i in range(len(positions))],
                         key=lambda x: x['position'])
        stack = []
        for robot in hashmap:
            if robot['direction'] == 'R':
                stack.append(robot)
                continue

            gone = False
            while stack and stack[-1]['health'] <= robot['health'] and stack[-1]['direction'] == 'R':
                if stack[-1]['health'] == robot['health']:
                    stack.pop()
                    gone = True
                    break
                robot['health'] -= 1
                stack.pop()

            if not gone and stack and stack[-1]['direction'] == 'R' and stack[-1]['health'] > robot['health']:
                stack[-1]['health'] -= 1
                gone = True

            if not gone:
                stack.append(robot)

        stack = sorted(stack, key=lambda x: x['idx'])
        healths = [robot['health'] for robot in stack]
        return healths


if __name__ == '__main__':
    solution = Solution()
    func_test = solution.survivedRobotsHealths
    cases = [
        {'data':
            {
                'positions': [3, 2, 30, 24, 38, 7],
                'healths': [47, 12, 49, 11, 47, 38],
                'directions': 'RRLRRR',
            },
            'result': [12, 47]},
        {'data':
            {
                'positions': [1, 40],
                'healths': [10, 11],
                'directions': 'RL',
            },
            'result': [10]},
        {'data':
            {
                'positions': [5, 4, 3, 2, 1],
                'healths': [2, 17, 9, 15, 10],
                'directions': 'RRRRR',
            },
            'result': [2, 17, 9, 15, 10]},
        {'data':
            {
                'positions': [3, 5, 2, 6],
                'healths': [10, 10, 15, 12],
                'directions': 'RLRL',
            },
            'result': [14]},
        {'data':
            {
                'positions': [1, 2, 5, 6],
                'healths': [10, 10, 11, 11],
                'directions': 'RLRL',
            },
            'result': []},
    ]
    failed = []
    for case in cases:
        fail = print_tests(func_test, case['data'], case['result'])
        if fail:
            failed.append(fail)

    if failed:
        print(f'{bcolors.WARNING}Total failed {len(failed)} of test cases{bcolors.ENDC}')
    for fail in failed:
        print(f'{fail["Case"]}: '
              f'Expected: {bcolors.OKGREEN}{fail["Expected"]}{bcolors.ENDC}, '
              f'Actual: {bcolors.FAIL}{fail["Actual"]}{bcolors.ENDC}')
