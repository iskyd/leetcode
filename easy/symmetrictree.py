"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def inner(p1: Optional[TreeNode], p2: Optional[TreeNode]):
            if p1 is None and p2 is None:
                return True
            elif p1 is None or p2 is None:
                return False
            return p1.val == p2.val and inner(p1.left, p2.right) and inner(p1.right, p2.left)

        if root is None:
            return True
        
        return inner(root.left, root.right)


s = Solution()
assert s.isSymmetric(TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(val=3), right=TreeNode(val=4)), right=TreeNode(val=2, left=TreeNode(val=4), right=TreeNode(val=3)))) == True
assert s.isSymmetric(TreeNode(val=1, left=TreeNode(val=2, right=TreeNode(val=3)), right=TreeNode(val=2, right=TreeNode(val=3)))) == False
assert s.isSymmetric(TreeNode(val=2, left=TreeNode(val=3, left=TreeNode(val=4), right=TreeNode(val=5)), right=TreeNode(val=3, right=TreeNode(val=4)))) == False
print("passed")
