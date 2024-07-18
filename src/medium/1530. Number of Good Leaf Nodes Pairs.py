from collections import deque

from src.tests import *
from src.bcolor import bcolors
from typing import Optional, Any


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def initTree(treeList: list[Optional[int]]) -> TreeNode:
    if len(treeList) == 0:
        return None
    root = TreeNode(treeList[0])
    queue = deque([root])
    i = 1
    while len(queue) > 0:
        node = queue.popleft()
        if i < len(treeList):
            if treeList[i] is not None:
                node.left = TreeNode(treeList[i])
                queue.append(node.left)
            i += 1
        if i < len(treeList):
            if treeList[i] is not None:
                node.right = TreeNode(treeList[i])
                queue.append(node.right)
            i += 1

    return root


class Solution:
    def __init__(self):
        self.res = 0

    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.res = 0

        def solve(root: TreeNode):
            if root is None:
                return {}
            if root.left is None and root.right is None:
                # leaf node here
                return {1: 1}
            lhNodes = solve(root.left)
            rhNodes = solve(root.right)

            for leftNodeHeight in lhNodes:
                if leftNodeHeight >= distance:
                    continue
                for rightNodeHeight in rhNodes:
                    if leftNodeHeight + rightNodeHeight <= distance:
                        self.res += lhNodes[leftNodeHeight] * rhNodes[rightNodeHeight]

            nhNodes = {}
            for key in lhNodes:
                if key <= distance:
                    nhNodes[key + 1] = lhNodes[key]
            for key in rhNodes:
                if key <= distance:
                    nhNodes[key + 1] = nhNodes.get(key + 1, 0) + rhNodes[key]

            return nhNodes

        solve(root)
        return self.res


if __name__ == '__main__':
    solution = Solution()
    func_test = solution.countPairs
    cases = [
        {'data':
            {
                'root': initTree([1, 2, 3, None, 4]),
                'distance': 3,
            },
            'result': 1},
        {'data':
            {
                'root': initTree([1, 2, 3, 4, 5, 6, 7]),
                'distance': 3,
            },
            'result': 2},
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
