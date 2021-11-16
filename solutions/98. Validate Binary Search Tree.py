# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #soln 2 - Recursive Inorder Traversal
        def inorder(node):
            if not node:
                return True
            if not inorder(node.left):
                return False
            if node.val <= self.prev:
                return False
            self.prev = node.val
            return inorder(node.right)
        self.prev = float('-inf')
        return inorder(root)
        
        # #soln 1 - Recursive Traversal with Valid Range
        # def validate(node, low=float('-inf'), high=float('inf')):
        #     if not node:
        #         return True
        #     if node.val <= low or node.val >= high:
        #         return False
        #     return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        # return validate(root)
        
        # # #soln 0 - standard inorder traversal, slow
        # def helper(node):
        #     if not node:
        #         return []
        #     return helper(node.left) + [node.val] + helper(node.right)
        # lst = helper(root)
        # return all([lst[i] < lst[i+1] for i in range(len(lst)-1)])
            
