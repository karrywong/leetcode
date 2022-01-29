# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        #Tricky, key idea: ask left & right subtree of their needs or excess and then compute its return to parent
        #Time O(N), space O(N)
        self.ans = 0
        def dfs(node) -> int: #deficiency/excess
            if not node:
                return 0 
            
            left = dfs(node.left)
            right = dfs(node.right)
            self.ans += abs(left) + abs(right)
            return node.val + left + right - 1
        dfs(root)
        return self.ans
