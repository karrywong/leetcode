# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.res = []
        
        #Input: root, output: list of node values in ascending order
        def helper(root,k):
            if root:
                if len(self.res) == k:
                    return self.res[-1]
                helper(root.left,k)
                if len(self.res) == k:
                    return self.res[-1]
                self.res.append(root.val)
                if len(self.res) == k:
                    return self.res[-1]
                helper(root.right,k)
                if len(self.res) == k:
                    return self.res[-1]
​
        return helper(root, k)
