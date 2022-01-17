# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #Leetcode recursion, time O(N), space O(N) due to recursion stack
#     def flattenTree(self, node):
#         if not node:
#             return None
        
#         if not node.left and not node.right:
#             return node
        
#         leftTail = self.flattenTree(node.left)
#         rightTail = self.flattenTree(node.right)
        
#         if leftTail:
#             leftTail.right = node.right
#             node.right = node.left
#             node.left = None
        
#         return rightTail if rightTail else leftTail
    
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # return self.flattenTree(root)
        
        #Leetcode solution time O(N), space O(1), super smart
        if not root:
            return None
        
        node = root
        while node:
            if node.left: #if node has left child
                #Find rightmost child
                rightmost = node.left 
                while rightmost.right:
                    rightmost = rightmost.right
                
                rightmost.right = node.right
                node.right = node.left
                node.left = None
                
            node = node.right
