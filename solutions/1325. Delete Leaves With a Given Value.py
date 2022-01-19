# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        #First attempt, inspired by DFS solution to 366. Find Leaves of Binary Tree
        #Time O(N), space O(N) due to recursion
        def helper(node):
            if node.left and helper(node.left):
                node.left = None
            if node.right and helper(node.right):
                node.right = None
            
            if node.val == target and node.left is None and node.right is None:
                return True
            else:
                return False
        
        return None if helper(root) else root
