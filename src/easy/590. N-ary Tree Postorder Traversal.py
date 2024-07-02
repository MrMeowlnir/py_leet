# Definition for a Node.
class Node(object):
    def __init__(self, val: int | None = None, children: list | None = None):
        if children is None:
            children = []
        self.val = val
        self.children = children


class Solution(object):
    def __init__(self, order: list[int | None] | None = None):
        self.order = order
        root = Node(order[0] if self.order else None)
        current_node = root
        for val in order[1:]:
            if val is not None:
                current_node.children.append(Node(val))
            else:
                if len(current_node.children) == 0:
                    current_node = root
                else:
                    current_node = current_node.children[0]  # Wrong order need to fix it

        self.root = root
        self.post_result = []

    def postorder(self, root: Node) -> list[int]:
        """
        :type root: Node
        :rtype: list[int]
        """
        for child in root.children:
            self.postorder(child)
        self.post_result.append(root.val)
        return self.post_result


if __name__ == "__main__":
    cases = [
        [1, None, 3, 2, 4, None, 5, 6],
        [1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None, None,
         14]
    ]

    for case in cases:
        solution = Solution(case)
        print(solution.postorder(solution.root if solution.root else None))
