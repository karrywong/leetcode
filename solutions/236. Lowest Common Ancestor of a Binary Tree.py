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
        
#         ptr = -1
#         prev = None
#         while abs(ptr) < len(p_lst)+1 and abs(ptr) < len(q_lst)+1 and p_lst[ptr].val == q_lst[ptr].val:
#             prev = p_lst[ptr]                
#             ptr -= 1
#         return prev
​
#         # Karry's solution w Haotian's
#         htb = {} #key=cur.val, value=prev.val
#         queue = collections.deque([root])
#         pval, qval = p.val, q.val
#         bo1, bo2 = False, False
        
#         while queue and (not bo1 or not bo2):
#             node = queue.popleft()
#             if node.val == pval: bo1 = True
#             elif node.val == qval: bo2 = True
#             if node.left:
#                 htb[node.left] = node
#                 queue.append(node.left)
#             if node.right:
#                 htb[node.right] = node
#                 queue.append(node.right)
#         #existing while loop, either queue is empty or p and q are both in htb
        
#         pset = set([p])
#         while p.val != root.val:
#             p = htb[p]
#             pset.add(p)
        
#         while q.val != root.val:
#             if q in pset: return q
#             q = htb[q]
#         return q
