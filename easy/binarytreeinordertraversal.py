"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""


from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
            

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        if not root:
            return l
        l.extend(self.inorderTraversal(root.left))
        l.append(root.val)
        l.extend(self.inorderTraversal(root.right))
        return l


# As suggested by leetcode I'm trying iterative solution
class Solution2:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        st = []
        while root or st:
            while root:
                st.append(root)
                root = root.left
            root = st.pop()
            ans.append(root.val)
            root = root.right
        return ans
        


s = Solution2()
assert s.inorderTraversal(TreeNode(val=1, left=None, right=TreeNode(val=2, left=TreeNode(val=3)))) == [1, 3, 2]
assert s.inorderTraversal(TreeNode(val=1)) == [1]
assert s.inorderTraversal(None) == []
print("succeded")

