# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        #Mock interview, time O(N), space O(N)
        if not root: return 0
        
        ans = 1
        def helper(node) -> (int, int, int): #output count, lo, hi
            nonlocal ans
            count, lo, hi = 1, node.val, node.val
            
            if node.left: 
                left_count, left_lo, left_hi = helper(node.left)
                if left_count > 0 and left_hi < node.val:
                    count += left_count
                    lo = left_lo
                else:
                    count = 0
            
            if node.right: 
                right_count, right_lo, right_hi = helper(node.right)
                if right_count > 0 and right_lo > node.val:
                    if count > 0:
                        count += right_count
                    hi = right_hi
                else:
                    count = 0
            
            ans = max(ans, count)
            return count, lo, hi
            
        helper(root)
        return ans
