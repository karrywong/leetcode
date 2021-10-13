# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #soln 1 - recursion
        #base case 
        if not root:
            return root
        else: # leave the root alone
            # then apply invertTree to left and right subtree
            # swap left tree and right tree
            #print(root.right, root.left)
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
