# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        ### First attempt
        if not root:
            return 0
        
        answer = 0
        if root.val <= high and root.val >= low:
            answer += root.val
        if root.val > low:
            answer += self.rangeSumBST(root.left, low, high)
        if root.val < high:
            answer += self.rangeSumBST(root.right, low, high)
        
        return answer
​
        ### Recursion - LeetCode answer
        # def dfs(node):
        #     if node:
        #         if low <= node.val <= high:
        #             self.ans += node.val
        #         if low < node.val:
        #             dfs(node.left)
        #         if node.val < high:
        #             dfs(node.right)
        # self.ans = 0
        # dfs(root)
        # return self.ans
                
    
