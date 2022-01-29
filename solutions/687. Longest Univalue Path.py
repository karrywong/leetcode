# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        #Failed attempts, Leetcode solution - idea: "any path as up to two arrows extending from its root"
        #Time O(N), space O(N)
        self.ans = 0
        def helper(node) -> int: #path length, node val
            if not node:
                return 0, float('inf')
​
            left_length  = helper(node.left)
            right_length = helper(node.right)
            left_arrow = right_arrow = 0
            if node.left and node.left.val == node.val:
                left_arrow = left_length + 1
            if node.right and node.right.val == node.val:
                right_arrow = right_length + 1
            self.ans = max(self.ans, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)
​
        helper(root)
        return self.ans
