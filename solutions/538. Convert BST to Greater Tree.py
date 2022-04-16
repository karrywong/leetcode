# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #Recursion, time O(N), space O(N)
        total = 0
        def helper(node: Optional[TreeNode]) -> Optional[TreeNode]:
            nonlocal total
            if node:
                helper(node.right)
                total += node.val
                node.val = total
                helper(node.left)
        helper(root)
        return root
        
#         #Time O(N), space O(N), first attempt w two traversal
#         def get_sum(node: Optional[TreeNode]) -> int:
#             if not node:
#                 return 0
#             return node.val + get_sum(node.left) + get_sum(node.right)
#         total_sum = get_sum(root)
        
#         stack = []
#         root_ref = root
#         prev = 0
        
#         #Iterative inorder traversal, see 94. Binary Tree Inorder Traversal
#         while stack or root_ref:
#             while root_ref:
#                 stack.append(root_ref)
#                 root_ref = root_ref.left
#             root_ref = stack.pop()
            
#             total_sum -= prev
#             prev = root_ref.val
#             root_ref.val = total_sum
            
#             root_ref = root_ref.right
#         return root
