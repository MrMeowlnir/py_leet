from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self, lst: list[int]):
        self.root = self.create_binary_tree(lst)

    def create_binary_tree(self, lst: list[int]) -> Optional[TreeNode]:
        if not lst:
            return None
        mid = len(lst) // 2
        root = TreeNode(lst[mid])
        root.left = self.create_binary_tree(lst[:mid])
        root.right = self.create_binary_tree(lst[mid + 1:])
        return root

    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)
        if depth == 2:
            root.left = TreeNode(val, left=root.left)
            root.right = TreeNode(val, right=root.right)
        if root.left:
            self.addOneRow(root.left, val, depth - 1)
        if root.right:
            self.addOneRow(root.right, val, depth - 1)
        return root


if __name__ == '__main__':
    cases = [dict({'root': [4, 2, 6, 3, 1, 5],
                   'val': 1,
                   'depth': 2}),
             dict({'root': [4, 2, None, 3, 1],
                   'val': 1,
                   'depth': 3}),
             ]

    for case in cases:
        solution = Solution(case['root'])
        print(solution.addOneRow(solution.root, case['val'], case['depth']))
