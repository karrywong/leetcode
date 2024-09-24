# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':         
        # time O(N), space O(N)
        self.ans = TreeNode()
        def helper(node: 'TreeNode') -> bool:
            if not node:
                return False
            left_val = helper(node.left)
            right_val = helper(node.right)
            val = True if node == p or node == q else False
            if left_val + right_val + val == 2:
                self.ans = node
            return val or left_val or right_val
        
        helper(root)
        return self.ans
​
​
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
​
#         ptr = -1
#         while abs(ptr-1) <= len(p_lst) and abs(ptr-1) <= len(q_lst) and p_lst[ptr-1].val == q_lst[ptr-1].val:
#             ptr -= 1
#         return p_lst[ptr]
​
​
#         # Karry's solution w Haotian's
#         htb = {} #key=cur.val, value=prev.val
#         queue = collections.deque([root])
#         pval, qval = p.val, q.val
