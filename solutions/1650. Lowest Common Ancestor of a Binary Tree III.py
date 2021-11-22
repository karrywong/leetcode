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
        #soln 0 - first attempt
        #idea from 236. Lowest Common Ancestor of a Binary Tree
        pset = set()
        while p is not None:
            pset.add(p)
            p = p.parent
            
        while q is not None:
            if q in pset: return q
            q = q.parent
