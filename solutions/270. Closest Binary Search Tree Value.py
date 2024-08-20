# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        # soln 1 - time O(N), space O(N)
        ans: float('inf')
        diff = float('inf')
        while root:
            # ans = min(ans, root.val, key = lambda x: abs(target - x))
            val = abs(root.val-target)
            if val < diff or (val == diff and root.val < ans):
                ans = root.val
                diff = val
                
            if root.val > target:
                root = root.left
            elif root.val < target:
                root = root.right
            else:
                return root.val
        return ans
                
