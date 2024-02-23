# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # soln 3 - Recursive inorder, time O(N), space O(N)
        def dfs(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            
            dfs(node.left)
            if self.prev_node and node.val < self.prev_node.val:
                if self.x is None:
                    self.x = self.prev_node
                self.y = node
            self.prev_node = node
            dfs(node.right)
        
        self.x = self.y = self.prev_node = None
        dfs(root)
        self.x.val, self.y.val = self.y.val, self.x.val
        
#         #soln 2 - Iterative inorder, time O(N), space (N)
#         stack = []
#         node = root
#         x = y = prev_node = None
#         while True:
#             if node is not None:
#                 stack.append(node)
#                 node = node.left
#             elif len(stack) > 0:
#                 node = stack.pop()
                
#                 if prev_node and node.val < prev_node.val:
#                     if x is None:
#                         x = prev_node
#                     y = node
    
#                 prev_node = node 
#                 node = node.right
#             else:
#                 break
#         x.val, y.val = y.val, x.val

#         #soln 1 - Trivial (first flatten tree->find two swapped nodes->dfs) w/ space O(N), time O(N)
#         def helper(node: Optional[TreeNode]) -> List[int]:
#             if not node:
#                 return []
#             return helper(node.left) + [node.val] + helper(node.right)
        
#         def dfs(node: Optional[TreeNode]) -> None:
#             if not node:
#                 return 
#             if node.val == x:
#                 node.val = y
#             elif node.val == y:
#                 node.val = x
#             dfs(node.left)
#             dfs(node.right)
            
#         lst = helper(root)
#         x, y = None, None
#         for i in range(len(lst)-1):
#             if lst[i] > lst[i+1]:
#                 if x is None:
#                     x = lst[i]
#                 y = lst[i+1]
#         dfs(root)
