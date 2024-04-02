# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
#         # bottom-to-top, time O(N), space O(N)
#         ans = 0
#         if root is None:
#             return ans
        
#         if root.val >= low:
#             ans += self.rangeSumBST(root.left, low, high)
#         if root.val <= high:
#             ans += self.rangeSumBST(root.right, low, high)
#         if low <= root.val <= high:
#             ans += root.val
#         return ans
​
        # top-to-bottom, time O(N), space O(N)
        ans = 0
        def dfs(node: Optional[TreeNode]) -> None:
            nonlocal ans
            if node is None:
                return
            if low <= node.val <= high:
                ans += node.val
            
            if node.val > low:
                dfs(node.left)
            if node.val < high:
                dfs(node.right)
        dfs(root)
        return ans
