# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:   
        #soln 2
        if p and q:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) if p.val == q.val else False
        elif not p and not q:
            return True
        else: 
            return False
        
        #soln 1
        if not p and not q:
            return True
        elif not p and q:
            return False
        elif p and not q:
            return False
        else:
            if p.val == q.val:
                return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
            else:
                return False
