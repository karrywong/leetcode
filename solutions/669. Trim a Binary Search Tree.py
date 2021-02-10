# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        ### Soln 1 - recursion
        def helper(root):
            if not root:
                return None
            elif root.val > high:
                return helper(root.left)
            elif root.val < low:
                return helper(root.right)
            else:
                root.left = helper(root.left)
                root.right = helper(root.right)
                return root
            
        return helper(root)
        
        # ### Soln 0 - first attempt by Jake Reschke
        # self.base = root
        # def helper(root,low,high):
        #     if root:
        #         if low <= root.val <= high:
        #             if root.left and root.left.val < low:
        #                 root.left = root.left.right
        #                 helper(root,low,high)
        #             else:
        #                 helper(root.left,low,high)
        #             if root.right and root.right.val > high:
