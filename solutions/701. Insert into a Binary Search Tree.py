# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # #soln 1 - Leetcode, recursion
        # if not root:
        #     return TreeNode(val)        
        # if root.val > val:
        #     root.left = self.insertIntoBST(root.left, val)
        # else:
        #     root.right = self.insertIntoBST(root.right, val)
        # return root
    
        #soln 0 - first attempt, recursion
        def helper(node):
            if node.val > val:
                if node.left is not None:
                    helper(node.left)
                else:
                    node.left = TreeNode(val)
            else:
                if node.right is not None:
                    helper(node.right)
                else:
                    node.right = TreeNode(val)
                
        if not root: 
            return TreeNode(val)
        helper(root)
        return root
