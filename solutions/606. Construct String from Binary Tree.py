# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        #First attempt, time O(N), space O(N)
        if not root.left and not root.right:
            return str(root.val)
        elif root.left and not root.right:
            return str(root.val) + "(" + self.tree2str(root.left) + ")"
        elif not root.left and root.right:
            return str(root.val) + "()(" + self.tree2str(root.right) + ")" 
        else:
            return str(root.val) + "(" + self.tree2str(root.left) + ")(" + self.tree2str(root.right) + ")"
