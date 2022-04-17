# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:        
#         #First-attempt Iterative inorder traversal, time O(N), space O(N)
#         stack = []
#         ans = TreeNode(None)
#         ptr = ans
        
#         while stack or root:
#             while root:
#                 stack.append(root)
#                 root = root.left
#             root = stack.pop()
#             ptr.right = TreeNode(root.val)
#             ptr = ptr.right
#             root = root.right
        
#         return ans.right
    
        #LeetCode inorder w recursion, time O(N), space O(N)
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)
        
        ans = cur = TreeNode(None)
        for v in inorder(root):
            cur.right = TreeNode(v)
            cur = cur.right
        return ans.right
​
#         #LeetCode inorder w recursion on the fly, time O(N), space O(N)
#         def inorder(node):
#             nonlocal cur
#             if node:
#                 inorder(node.left)
#                 node.left = None
#                 cur.right = node
#                 cur = cur.right
#                 inorder(node.right)
                
#         ans = cur = TreeNode(None)
#         inorder(root)
#         return ans.right        
