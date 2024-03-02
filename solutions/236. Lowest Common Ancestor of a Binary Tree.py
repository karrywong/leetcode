# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode': 
        #One pass with DFS
        self.ans = None
        def dfs(node: 'TreeNode', t1: int, t2: int) -> bool:
            if node is None:
                return False
            left_bo = dfs(node.left, t1, t2)
            right_bo = dfs(node.right, t1, t2)
            cur = True if node.val == t1 or node.val == t2 else False
            if left_bo+right_bo+cur >= 2: 
                self.ans = node
            return left_bo or right_bo or cur
        
        dfs(root, p.val, q.val)
        return self.ans
        
#         #Two-pass DFS, Time O(N), space O(N)
#         def dfs(node: 'TreeNode', target: int) -> List['TreeNode']:
#             if node is None:
#                 return []
#             if node.val == target:
#                 return [node]
            
#             left_lst = dfs(node.left, target)
#             right_lst = dfs(node.right, target) 
            
#             if len(left_lst) > 0:
#                 left_lst.append(node)
#                 return left_lst 
#             if len(right_lst) > 0:
#                 right_lst.append(node)
#                 return right_lst
#             return []
            
#         p_lst = dfs(root, p.val)
#         q_lst = dfs(root, q.val)
        
#         ptr = -1
#         prev = None
#         while abs(ptr) < len(p_lst)+1 and abs(ptr) < len(q_lst)+1 and p_lst[ptr].val == q_lst[ptr].val:
#             prev = p_lst[ptr]                
#             ptr -= 1
#         return prev
​
