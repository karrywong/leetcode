# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #soln 0 - Jake's soln 
        pval = p.val
        qval = q.val
        memo = {None:False} # memo[subtree_root] = True if subtree contains p or q
​
        def helper(subtree):
            if subtree in memo: return memo[subtree]
            if subtree.val in [pval,qval]:
                memo[subtree] = True
            else:
                memo[subtree] = helper(subtree.left) or helper(subtree.right)
            return memo[subtree]
        curnode = root
        while True:
            if curnode.val in [pval,qval]:
                return curnode
            left = helper(curnode.left)
            right = helper(curnode.right)
            if left and right:
                return curnode
            if left:
                curnode = curnode.left
            else:
                curnode = curnode.right
