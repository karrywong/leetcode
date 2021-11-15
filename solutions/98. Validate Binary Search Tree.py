# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # #soln 0 - standard inorder traversal
        def helper(node):
            if not node:
                return []
            return helper(node.left) + [node.val] + helper(node.right)
        lst = helper(root)
        return all([lst[i] < lst[i+1] for i in range(len(lst)-1)])
            
