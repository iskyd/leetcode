"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def fromlist(l: list) -> 'ListNode|None':
        if len(l) == 0:
            return None
        r = ListNode(l[0])
        h = r
        for i in range(1, len(l)):
            r.next = ListNode(l[i], None)
            r = r.next
        return h

    def tolist(self) -> list:
        l = list()
        node = self
        while node:
            l.append(node.val)
            node = node.next
        return l


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h = ListNode()
        n = h
        while list1 or list2:
            if not list1:
                n.next = ListNode(list2.val, None)
                n = n.next
                list2 = list2.next
            elif not list2:
                n.next = ListNode(list1.val, None)
                n = n.next
                list1 = list1.next
            else:
                if list1.val <= list2.val:
                    n.next = ListNode(list1.val, None)
                    n = n.next
                    list1 = list1.next
                else:
                    n.next = ListNode(list2.val, None)
                    n = n.next
                    list2 = list2.next
                

        return h.next


s = Solution()
assert s.mergeTwoLists(ListNode.fromlist([1,2,4]), ListNode.fromlist([1,3,4])).tolist() == [1,1,2,3,4,4]
assert s.mergeTwoLists(ListNode.fromlist([]), ListNode.fromlist([])) == None
assert s.mergeTwoLists(ListNode.fromlist([]), ListNode.fromlist([0])).tolist() == [0]
print("passed")

