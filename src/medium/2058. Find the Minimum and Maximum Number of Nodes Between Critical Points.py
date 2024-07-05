# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val: Optional[int] = 0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, data_list: Optional[list[int]]):
        self.head = None
        self.append_list(data_list)

    def append_list(self, data_list: Optional[list[int]]) -> None:
        if data_list is None:
            return
        for data in data_list:
            self.append(data)

    def append(self, data: Optional[int]) -> None:
        if self.head is None:
            self.head = ListNode(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = ListNode(data)


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> list[int]:
        distance = [-1, -1]
        node = head
        ptr = 0
        critical_point = -1
        fcc = -1
        while node.next.next:
            ptr += 1
            if ((node.val < node.next.val and node.next.val > node.next.next.val) or
                    (node.val > node.next.val and node.next.val < node.next.next.val)):
                if critical_point == -1:
                    critical_point = ptr
                    fcc = ptr
                else:
                    if distance[0] == -1:
                        distance[0] = ptr - critical_point
                    elif distance[0] > ptr - critical_point:
                        distance[0] = ptr - critical_point
                    distance[1] = ptr - fcc
                    critical_point = ptr
            node = node.next
        return distance


if __name__ == '__main__':
    solution = Solution()
    cases = [dict({'data_list': [3, 1]}),
             dict({'data_list': [5, 3, 1, 2, 5, 1, 2]}),
             dict({'data_list': [1, 3, 2, 2, 3, 2, 2, 2, 7]}),
             ]
    for case in cases:
        ll = LinkedList(case['data_list'])
        print(solution.nodesBetweenCriticalPoints(ll.head))
