"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

            

s = Solution()
assert s.isSameTree(TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3)), TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3))) == True
assert s.isSameTree(TreeNode(val=1, left=TreeNode(val=2)), TreeNode(val=1, right=TreeNode(val=2))) == False
assert s.isSameTree(TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=1)), TreeNode(val=1, left=TreeNode(val=1), right=TreeNode(val=2))) == False
print("succeded")
