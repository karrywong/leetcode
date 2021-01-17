# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def postorder(root):
            return postorder(root.left) + postorder(root.right) + [root.val] if root else []
        return postorder(root)
        
