# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        ### Soln 1 - record complement for root1 in a hashtable and search through root2
        self.lib = {}
        def dfs(root, k):
            if root:
                self.lib[k - root.val] = root.val
                return dfs(root.left, k) or dfs(root.right, k)
        dfs(root1, target)
        
        def valid(root,k):
            if root:
                if root.val in self.lib:
                    return True
                return valid(root.left, k) or valid(root.right, k)
        
        return valid(root2, target)
        
        
        
