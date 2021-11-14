# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #soln 1 - Leetcode recursion, cleaner
        if not root or root.val == val:
            return root
        return self.searchBST(root.left, val) if root.val > val else self.searchBST(root.right, val)
        
        # #soln 0 - first attempt, recursion
        # def helper(node):
        #     if not node:
        #         return None
        #     if node.val == val:
        #         return node
        #     elif node.val < val:
        #         return helper(node.right)
        #     else:
        #         return helper(node.left)
        # return helper(root)
            
        
