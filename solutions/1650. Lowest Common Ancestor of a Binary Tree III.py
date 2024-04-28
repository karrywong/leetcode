"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""
​
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # soln 1 - time O(N), space O(1) 
        p_ptr = p
        q_ptr = q
        
        while p_ptr.val != q_ptr.val:
            p_ptr = p_ptr.parent
            if p_ptr is None:
                p_ptr = q
            q_ptr = q_ptr.parent
            if q_ptr is None:
                q_ptr = p
            
        return p_ptr
# Testing
# p_ptr = 5, 3, 4, 2, 5
# q_ptr = 4, 2, 5, 3, 5
​
# p_ptr = 1, 3, 7, 2, 5, 3
# q_ptr = 7, 2, 5, 3, 1, 3
    
#         #soln 0 - time O(N), space O(H)
#         #idea from 236. Lowest Common Ancestor of a Binary Tree
#         pset = set()
#         while p is not None:
#             pset.add(p)
#             p = p.parent
            
#         while q is not None:
#             if q in pset: return q
#             q = q.parent
