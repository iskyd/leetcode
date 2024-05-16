"""
Given a binary tree, determine if it is height-balanced.
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def recursive(root: Optional[TreeNode]) -> tuple[bool, int]:
            if not root:
                return True, 0
            bl, hl = recursive(root.left)
            br, hr = recursive(root.right)
            
            return bl and br and abs(hl-hr) <= 1, 1 + max(hl, hr)
            
        return recursive(root)[0]


s = Solution()
assert s.isBalanced(TreeNode(val=3, left=TreeNode(val=9), right=TreeNode(val=20, left=TreeNode(val=15), right=TreeNode(val=7)))) == True
assert s.isBalanced(TreeNode(val=1, right=TreeNode(val=2), left=TreeNode(val=2, right=TreeNode(val=3), left=TreeNode(val=3, left=TreeNode(val=4), right=TreeNode(val=4))))) == False
assert s.isBalanced(None) == True
print("succeded")
