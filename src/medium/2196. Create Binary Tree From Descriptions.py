from src.tests import *
from src.bcolor import bcolors
from typing import Optional, Any


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> Optional[TreeNode]:
        """
        You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti]
        indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,

        If isLefti == 1, then childi is the left child of parenti.
        If isLefti == 0, then childi is the right child of parenti.
        Construct the binary tree described by descriptions and return its root.

        The test cases will be generated such that the binary tree is valid.
        """
        nodes = dict()
        children = set()

        for parent, child, isLeft in descriptions:
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if child not in nodes:
                nodes[child] = TreeNode(child)
            if isLeft:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]
            children.add(child)

        root = None
        for parent, _, _ in descriptions:
            if parent not in children:
                root = nodes[parent]
                break
        queue, result = list(), list()
        queue.append(root)
        result.append(root.val)
        while queue:
            node = queue.pop(0)
            if node.left or node.right:
                result.append(node.left.val if node.left else None)
                result.append(node.right.val if node.right else None)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        while not result[-1]:
            result.pop()
        return result


if __name__ == '__main__':
    solution = Solution()
    func_test = solution.createBinaryTree
    cases = [
        {'data':
            {
                'descriptions': [[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]]
            },
            'result': [50, 20, 80, 15, 17, 19]},
        {'data':
            {
                'descriptions': [[1, 2, 1], [2, 3, 0], [3, 4, 1]],
            },
            'result': [1, 2, None, None, 3, 4]},
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
