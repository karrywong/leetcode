# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':         
        # Karry's solution w Haotian's
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
        
        pset = set([p])
        while p.val != root.val:
            p = htb[p]
            pset.add(p)
        
        while q.val != root.val:
            if q in pset: return q
            q = htb[q]
        return q
​
        # #Leetcode - DFS w recursion
        # self.ans = None
        # global pval, qval
        # def dfs(node):
        #     if not node: 
        #         return False
        #     left = dfs(node.left)
        #     right = dfs(node.right)
        #     mid = True if node.val == pval or node.val == qval else False
        #     if left + right + mid >= 2:
        #         self.ans = node
        #     return mid or left or right
        # pval, qval = p.val, q.val
        # dfs(root)
        # return self.ans
​
#         #soln 0 - Jake's soln 
#         pval = p.val
#         qval = q.val
#         memo = {None:False} # memo[subtree_root] = True if subtree contains p or q
        
#         def helper(subtree):
#             if subtree in memo: return memo[subtree]
#             if subtree.val in [pval,qval]:
#                 memo[subtree] = True
#             else:
#                 memo[subtree] = helper(subtree.left) or helper(subtree.right)
#             return memo[subtree]
#         curnode = root
#         while True:
#             if curnode.val in [pval,qval]:
#                 return curnode
#             left = helper(curnode.left)
#             right = helper(curnode.right)
#             if left and right:
#                 return curnode
#             if left:
#                 curnode = curnode.left
#             else:
#                 curnode = curnode.right
