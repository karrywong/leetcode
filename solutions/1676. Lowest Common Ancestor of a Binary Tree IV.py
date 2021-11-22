# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':        
        #Leetcode - DFS w recursion
        #Idea from DFS solution for 236. Lowest Common Ancestor of a Binary Tree
        self.ans = None
        global vals, n
        def dfs(node):
            if not node: 
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            mid = 1 if node.val in vals else 0
            if left + right + mid >= n:
                self.ans = node
                return 0
            return mid+left+right
        
        vals = [node.val for node in nodes]
        n = len(nodes)
        dfs(root)
        return self.ans
        
