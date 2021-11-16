# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # #soln 1 - iterative
        # pval, qval = p.val, q.val
        # node = root
        # while node:
        #     val = node.val
        #     if pval < val and qval < val: 
        #         node = node.left
        #     elif pval > val and qval > val:
        #         node = node.right
        #     else:
        #         return node
        
        #soln 0 - recursion
        pval, qval = p.val, q.val
        if pval < root.val and qval < root.val: 
            return self.lowestCommonAncestor(root.left, p, q)
        elif pval > root.val and qval > root.val: 
            return self.lowestCommonAncestor(root.right, p, q)
        else: 
            return root
