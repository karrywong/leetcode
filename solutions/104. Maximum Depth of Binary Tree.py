# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        ### Soln 0 - first attempt, recursion
        depth = 0
        def helper(root, depth):
            if root:
                depth += 1
​
            return max(depth, helper(root.left, depth), helper(root.right, depth)) if root else depth
​
        
        depth = helper(root, depth)
        return depth
