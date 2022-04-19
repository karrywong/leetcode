# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
#         #soln 1 - Trivial (first flatten tree->find two swapped nodes->dfs) w/ space O(N), time O(N)
#         def helper(node):
#             if not node: return []
#             return helper(node.left) + [node.val] + helper(node.right)
        
#         def dfs(node):
#             if not node: return
#             if node.val in diff:
#                 node.val = diff[1] if node.val == diff[0] else diff[0]
#             dfs(node.left)
#             dfs(node.right)
            
#         lst = helper(root)
#         diff = [None, None]
#         for i in range(len(lst)-1):
#             if lst[i] > lst[i+1]:
#                 diff[1] = lst[i+1]
#                 if diff[0] is None:
#                     diff[0] = lst[i]
#                 else:
#                     break
#         dfs(root)
​
        #soln 2 - LeetCode's iterative inorder, time O(N), space (N)
        stack = []
        x = y = pred = None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pred and root.val < pred.val:
                y = root
                if x is None:
                    x = pred
                else:
                    break
            pred = root
            root = root.right
        
        x.val, y.val = y.val, x.val
