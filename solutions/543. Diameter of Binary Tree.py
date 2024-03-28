# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #Mock w/ Haotian 8/28/2022
        #1. ans = max(ans, left_len + right_len + 1)
        #2. return max(left_len, right_len)
        ans = 0 #longestLen
        #longest_path = []
        def helper(node: TreeNode) -> int:
            nonlocal ans
            if not node: 
                return 0
            left_len = helper(node.left)
            right_len = helper(node.right)
            # left_len, left_path = helper(node.left)
            # right_len, right_path = helper(node.right)
            ans = max(ans, left_len+right_len)
            
            #path = left_path + [node.val] if left_len > right_len else right_path + [node.val]
            # if left_len+right_len > longestLen:
            #    longest_path = left_path + [node.val] + right_path[::-1]
            
            return max(left_len, right_len) + 1
            #return longestLen, path
        
        helper(root)
        return ans
