# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        #Karry's recursive preorder traversal, learned from Leetcode
        def preorder(node, cur_sum = 0):
            nonlocal ans
            if node:
                cur_sum = (cur_sum << 1) | node.val
                if not node.right and not node.left:
                    ans += cur_sum
                preorder(node.left, cur_sum)
                preorder(node.right, cur_sum)
        ans = 0
        preorder(root)
        return ans
        
