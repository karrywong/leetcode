# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #Almost exactly identical to my soln at 236. Lowest Common Ancestor of a Binary Tree
        #Line "if not bo1 or not bo2: return None" added
        htb = {} #key=cur.val, value=prev.val
        queue = collections.deque([root])
        pval, qval = p.val, q.val
        bo1, bo2 = False, False
        
        while queue and (not bo1 or not bo2):
            node = queue.popleft()
            if node.val == pval: bo1 = True
            elif node.val == qval: bo2 = True
            if node.left:
                htb[node.left] = node
                queue.append(node.left)
            if node.right:
                htb[node.right] = node
                queue.append(node.right)
        #existing while loop, either queue is empty or p and q are both in htb
        
        if not bo1 or not bo2: return None
        pset = set([p])
        while p.val != root.val:
            p = htb[p]
            pset.add(p)
        
        while q.val != root.val:
            if q in pset: return q
            q = htb[q]
        return q
