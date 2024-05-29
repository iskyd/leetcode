"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
"""


from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        if root.left is None and root.right is None:
            return 1

        if root.left and root.right:
            return min(1 + self.minDepth(root.left), 1 + self.minDepth(root.right))
        elif root.left:
            return 1 + self.minDepth(root.left)
        else:
            return 1 + self.minDepth(root.right)



s = Solution()
assert s.minDepth(TreeNode(val=3, left=TreeNode(val=9), right=TreeNode(val=20, left=TreeNode(val=15), right=TreeNode(val=7)))) == 2
assert s.minDepth(TreeNode(val=2, right=TreeNode(val=3, right=TreeNode(val=4, right=TreeNode(val=5, right=TreeNode(val=6)))))) == 5
assert s.minDepth(None) == 0
print("passed")
