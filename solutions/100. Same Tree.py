# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            if p.val == q.val:
                return True and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) 
            else: 
                return False
        elif not p and not q:
            return True
        else: 
            return False
            
        
        
