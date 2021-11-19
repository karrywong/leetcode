# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #first attempt, DFS, but redundant hence slow
        def isSameSubtree(p, q):
            if p and q:
                return isSameSubtree(p.left, q.left) and isSameSubtree(p.right, q.right) if p.val == q.val else False
            elif not p and not q:
                return True
            else:
                return False
        if not root:
            return False
        if root.val == subRoot.val:
            return isSameSubtree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)                
​
