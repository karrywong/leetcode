# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        #soln 1 - iterative w DFS
        if not root: return False
        stack = [(root, targetSum-root.val)]
        while stack:
            node, val = stack.pop()
            if not node.right and not node.left and val == 0:
                return True
            if node.left:
                stack.append((node.left, val-node.left.val))
            if node.right:
                stack.append((node.right, val-node.right.val))
        return False
        
#         # DFS helper function
#         def dfs(node: Optional[TreeNode], cur_sum:int=0) -> bool:
#             if node:
#                 cur_sum += node.val
#                 if node.left is None and node.right is None and cur_sum == targetSum:
#                     return True
#                 return dfs(node.left, cur_sum) or dfs(node.right, cur_sum)
#             return False
#         return dfs(root)
​
#         # DFS, time O(N), space O(N)
#         if root is None:
#             return False
#         if root.left is None and root.right is None and root.val == targetSum:
#             return True
#         return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)
        
