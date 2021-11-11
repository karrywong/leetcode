# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addLeaves(self, res, root):
        if not root.left and not root.right:
            res.append(root.val)
        else:
            if root.left:
                self.addLeaves(res, root.left)
            if root.right:
                self.addLeaves(res, root.right)
       
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        #Leetcode simple solution
        if not root: return root
        res = []
        if root.left or root.right:
            res.append(root.val)
        
        #Add left boundary
        t = root.left
        while t:
            if t.left or t.right:
                res.append(t.val)
            if t.left:
                t = t.left
            else:
                t = t.right
        
        #Add leaves from left to right
        self.addLeaves(res, root)
        stack = []
        t = root.right
        while t:
            if t.left or t.right:
                stack.append(t.val)
            if t.right:
                t = t.right
            else:
                t = t.left
        while stack:
            res.append(stack.pop())
        return res
