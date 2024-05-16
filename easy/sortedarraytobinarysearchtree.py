"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Just needed for assertion
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        
        s = len(nums) // 2
        return TreeNode(val=nums[s], left=self.sortedArrayToBST(nums[:s]), right=self.sortedArrayToBST(nums[s + 1:]))


s = Solution()
assert s.isSameTree(s.sortedArrayToBST([-10,-3,0,5,9]), TreeNode(val=0, left=TreeNode(val=-3, left=TreeNode(val=-10)), right=TreeNode(val=9, left=TreeNode(val=5)))) == True
print("succeded")
