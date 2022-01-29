# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
#         #Leetcode Inorder optimized, time O(N^2), space O(N)
#         def isValidBST(node) -> bool:
#             nonlocal previous
#             if not node:
#                 return True
#             if not isValidBST(node.left):
#                 return False
#             if node.val <= previous:
#                 return False
#             previous = node.val
#             return isValidBST(node.right)
        
#         def countNodes(node) -> int:
#             if not node:
#                 return 0
#             return 1 + countNodes(node.left) + countNodes(node.right)
        
#         if not root:
#             return 0
#         previous = float('-inf')
#         if isValidBST(root):
#             return countNodes(root)
#         return max(self.largestBSTSubtree(root.left), self.largestBSTSubtree(root.right))
        
        #LeetCode post-order, time O(N), space O(N)
        def helper(node) ->  (int, int, int): #output count, lo, hi
            if not node:
                return 0, float('inf'), float('-inf')
            
            left = helper(node.left)
            right = helper(node.right)
            
            if left[2] < node.val < right[1]:
                return 1+left[0]+right[0], min(node.val, left[1]), max(node.val, right[2])
            
            return max(left[0], right[0]), float('-inf'), float('inf')
        return helper(root)[0]
    
#         #Mock interview, time O(N), space O(N)
#         if not root: return 0
#         ans = 1
#         def helper(node) ->c
#             nonlocal ans
#             count, lo, hi = 1, node.val, node.val
            
#             if node.left: 
#                 left_count, left_lo, left_hi = helper(node.left)
#                 if left_count > 0 and left_hi < node.val:
#                     count += left_count
#                     lo = left_lo
#                 else:
#                     count = 0
            
#             if node.right: 
#                 right_count, right_lo, right_hi = helper(node.right)
#                 if right_count > 0 and right_lo > node.val:
#                     if count > 0: #key is to only add if node.left is BST or node does not have node.left
#                         count += right_count
#                     hi = right_hi
#                 else:
#                     count = 0
            
#             ans = max(ans, count)
#             return count, lo, hi
            
#         helper(root)
#         return ans
