"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
"""


from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        if targetSum - root.val == 0 and root.right is None and root.left is None:
            return True
        elif targetSum - root.val <= 0:
            return False

        return any((self.hasPathSum(root.left, targetSum - root.val), self.hasPathSum(root.right, targetSum - root.val)))


s = Solution()
assert s.hasPathSum(TreeNode(val=5, left=TreeNode(val=4, left=TreeNode(val=11, left=TreeNode(val=7), right=TreeNode(val=2))), right=TreeNode(val=8, left=TreeNode(val=13), right=TreeNode(val=4, right=TreeNode(val=1)))), 22) == True
assert s.hasPathSum(TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3)), 5) == False
assert s.hasPathSum(None, 0) == False
assert s.hasPathSum(TreeNode(val=1, left=TreeNode(val=2)), 0) == False
print("passed")
