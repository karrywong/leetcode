# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time O(N), N = |V|, space O(N)
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return None
        left_tail = self.flatten(root.left)
        right_tail = self.flatten(root.right)
        
        if left_tail is None:
            left_tail = root
        else:
            left_tail.right = root.right
            root.right = root.left
            root.left = None
        
        return right_tail if right_tail is not None else left_tail
​
#         """
#         Do not return anything, modify root in-place instead.
#         """        
#         #Morris traversal, time O(N), space O(1), super smart
#         if not root:
#             return None
        
#         node = root
#         while node:
#             if node.left: #if node has left child
#                 #Find rightmost child
#                 rightmost = node.left 
#                 while rightmost.right:
#                     rightmost = rightmost.right
                
#                 rightmost.right = node.right
#                 node.right = node.left
#                 node.left = None
                
#             node = node.right
