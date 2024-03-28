# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        #soln 1 - time O(N), space O(N)
        ans = 0
        def dfs(node: Optional[TreeNode], prev_val:int=0) -> None:
            nonlocal ans
            if node:
                prev_val = prev_val*10 + node.val
                
                if node.left is None and node.right is None:
                    ans += prev_val
                
                dfs(node.left,prev_val)
                dfs(node.right,prev_val)
            return
        dfs(root)
        return ans
        
        # #soln 0 - first attempt,  recursive preorder traversal: node -> left -> right
        # #More challenging, 437. Path Sum III
        # def helper(root, val=0):
        #     nonlocal ans
        #     if not root:
        #         return
        #     val += root.val
        #     if not root.right and not root.left:
        #         ans += val 
        #     helper(root.left, val*10)
        #     helper(root.right, val*10)
        # ans = 0
        # helper(root)
        # return ans
