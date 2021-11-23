# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        #Leetcode recursion, cleanest but hard to understand
        Result = collections.namedtuple("Result", ("node", "dist"))
        def dfs(node):
            # Return the result of the subtree at this node.
            if not node: return Result(None, 0)
            L, R = dfs(node.left), dfs(node.right)
            if L.dist > R.dist: return Result(L.node, L.dist + 1)
            if L.dist < R.dist: return Result(R.node, R.dist + 1)
            return Result(node, L.dist + 1)
​
        return dfs(root).node
        
#         #Karry's first attempt with Jake's help, DFS with memoization on depth, two passes
#         htb = {} #key = node, value = depth
#         def dfs(node):
#             if not node:
#                 return 0
#             if node not in htb:
#                 left = dfs(node.left)
#                 right = dfs(node.right)
#                 depth = max(left, right) + 1
#                 htb[node] = depth
#                 return depth
#             return htb[node]
#         dfs(root) #htb built
        
#         while root:
#             left_depth = htb[root.left] if root.left else 0
#             right_depth = htb[root.right] if root.right else 0
#             if left_depth == right_depth:
#                 return root
#             elif left_depth > right_depth:
#                 root = root.left
#             else: #left_depth < right_depth
#                 root = root.right
