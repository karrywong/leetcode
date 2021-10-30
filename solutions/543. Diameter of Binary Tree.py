# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # soln 0 - LeetCode DFS, time O(N), space O(N)
        self.diameter = 0 
        def helper(node):
            if not node:
                return 0
            
            left_path = helper(node.left)
            right_path = helper(node.right)
            self.diameter = max(self.diameter, left_path + right_path)
            
            return max(left_path, right_path) + 1
        helper(root)
        return self.diameter
