#         stack = []
#         node = root
#         x = y = prev_node = None
#         while True:
#             if node is not None:
#                 stack.append(node)
#                 node = node.left
#             elif len(stack) > 0:
#                 node = stack.pop()
                
#                 if prev_node and node.val < prev_node.val:
#                     if x is None:
#                         x = prev_node
#                     y = node
    
#                 prev_node = node 
#                 node = node.right
#             else:
#                 break
#         x.val, y.val = y.val, x.val
​
#         #soln 1 - Trivial (first flatten tree->find two swapped nodes->dfs) w/ space O(N), time O(N)
#         def helper(node: Optional[TreeNode]) -> List[int]:
#             if not node:
#                 return []
#             return helper(node.left) + [node.val] + helper(node.right)
        
#         def dfs(node: Optional[TreeNode]) -> None:
#             if not node:
#                 return 
#             if node.val == x:
#                 node.val = y
#             elif node.val == y:
#                 node.val = x
#             dfs(node.left)
#             dfs(node.right)
            
#         lst = helper(root)
#         x, y = None, None
#         for i in range(len(lst)-1):
#             if lst[i] > lst[i+1]:
#                 if x is None:
#                     x = lst[i]
#                 y = lst[i+1]
#         dfs(root)
