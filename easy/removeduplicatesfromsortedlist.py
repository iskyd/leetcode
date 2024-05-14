"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        n = {}
        cur = head
        prev = None
        while cur:
            if n.get(cur.val, False) is True:
                # Duplicates
                assert prev is not None
                prev.next = cur.next
                cur = cur.next
            else:
                n[cur.val] = True
                prev = cur
                cur = cur.next
            
        return head

s = Solution()
print(s.deleteDuplicates(ListNode.fromlist([1, 1, 1])).tolist())
assert s.deleteDuplicates(ListNode.fromlist([1, 1, 2])).tolist() == [1, 2]
assert s.deleteDuplicates(ListNode.fromlist([1, 1, 2, 3, 3])).tolist() == [1, 2, 3]
assert s.deleteDuplicates(ListNode.fromlist([1, 1, 1])).tolist() == [1]
print("succeded")
