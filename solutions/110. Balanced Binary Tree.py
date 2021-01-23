# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
class Solution:
    def isBalancedHelper(self, root: TreeNode) -> (bool, int):
        # An empty tree is balanced and has height -1
        if not root:
            return True, -1
        
        # Check subtrees to see if they are balanced. 
        leftIsBalanced, leftHeight = self.isBalancedHelper(root.left)
        if not leftIsBalanced:
            return False, 0
        rightIsBalanced, rightHeight = self.isBalancedHelper(root.right)
        if not rightIsBalanced:
            return False, 0
        
        # If the subtrees are balanced, check if the current tree is balanced
        # using their height
        return (abs(leftHeight - rightHeight) < 2), 1 + max(leftHeight, rightHeight)
            
    
    def isBalanced(self, root: TreeNode) -> bool:
        ### Soln 1 - Bottom-up recursion, LeetCode solution! Clever
        return self.isBalancedHelper(root)[0]
        
#         ### Soln 0 - first attempt, get the height of left and right subtree at every node
#         ### Top-down recursion
#         def height(root):
#             if not root:
#                 return 0
​
#             left_height = height(root.left)
#             right_height = height(root.right)
#             return max(left_height, right_height) + 1
        
#         if not root:
#             return True
        
#         lh = height(root.left)
#         rh = height(root.right)
#         # print(root.val, lh, rh)
#         return abs(lh - rh) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
