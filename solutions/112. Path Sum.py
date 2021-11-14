# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        #soln 1 - iterative w DFS
        if not root: return False
        stack = [(root, targetSum-root.val)]
        while stack:
            node, val = stack.pop()
            if not node.right and not node.left and val == 0:
                return True
            if node.right:
                stack.append((node.right, val-node.right.val))
            if node.left:
                stack.append((node.left, val-node.left.val))
        return False
        
        # #soln 0 - first attempt, recursion
        # if root is None:
        #     return False
        # elif root.left is None and root.right is None:
        #     return root.val == targetSum
        # else:
        #     return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)
