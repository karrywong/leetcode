# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # #soln 1 - Leetcode recursive preorder traversal
        # def preorder(r, cur_sum):
        #     nonlocal root_to_leaf
        #     if r:
        #         cur_sum = cur_sum * 10 + r.val
        #         if not r.right and not r.left:
        #             root_to_leaf += cur_sum
        #         preorder(r.left, cur_sum)
        #         preorder(r.right, cur_sum)
        # root_to_leaf = 0
        # preorder(root, 0)
        # return root_to_leaf
        
        #soln 0 - first attempt,  recursive preorder traversal: node -> left -> right
        #More challenging, 437. Path Sum III
        def helper(root, val=0):
            nonlocal ans
            if not root:
                return
            val += root.val
            if not root.right and not root.left:
                ans += val 
            helper(root.left, val*10)
            helper(root.right, val*10)
        ans = 0
        helper(root)
        return ans
