# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #soln 1 - recursion bottom-up
        def helper(node):
            if not node: 
                return True, -1
            leftIsBalanced, leftHeight = helper(node.left)
            if not leftIsBalanced:
                return False, 0
            rightIsBalanced, rightHeight = helper(node.right)
            if not rightIsBalanced:
                return False, 0  
            return (abs(leftHeight - rightHeight) < 2), 1 + max(leftHeight, rightHeight)
        return helper(root)[0]
​
        # #soln 0 - first attempt, recursion top-down
        # def helper(node): #compute tree height
        #     if not node: return 0
        #     return max(helper(node.right), helper(node.left)) + 1
        # if not root: return True
        # left_height = helper(root.left)
        # right_height = helper(root.right)
        # if abs(left_height - right_height) <= 1:
        #     return self.isBalanced(root.left) and self.isBalanced(root.right)
        # else:
        #     return False
​
        
