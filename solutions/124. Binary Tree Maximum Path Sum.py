# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #Could not figure out max(helper(node.left), 0) and max(helper(node.right), 0)
        #Inspired by soln for 543. Diameter of Binary Tree and 687. Longest Univalue Path
        self.ans = float('-inf')
        def helper(node) -> int: #path sum
            if not node:
                return 0
            
            left_sum = max(helper(node.left), 0)
            right_sum = max(helper(node.right), 0)
            left_arrow = right_arrow = 0
            if node.left:
                left_arrow += left_sum
            if node.right:
                right_arrow += right_sum
            
            self.ans = max(self.ans, left_sum + right_sum + node.val)
            return max(left_sum, right_sum) + node.val
        
        helper(root)
        return self.ans
