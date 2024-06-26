# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
#         #soln 1 - Leetcode iterative
#         stack = []
#         if root is not None:
#             stack.append((1,root))
        
#         depth = 0
#         while stack != []:
#             current_depth, root = stack.pop()
#             if root is not None:
#                 depth = max(depth, current_depth)
#                 stack.append((current_depth + 1, root.left))
#                 stack.append((current_depth + 1, root.right))
#         return depth
        
        #soln 0 - Recursion DFS, simplest
        if not root:
            return 0
        return max(self.maxDepth(root.right), self.maxDepth(root.left)) + 1
