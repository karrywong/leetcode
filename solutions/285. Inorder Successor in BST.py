# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':
        #LeetCode BST 
        successor = None
        while root:
            if p.val >= root.val:
                root = root.right
            else:
                successor = root
                root = root.left
        return successor
    
        # #First attempt, time O(N), space O(1)
        # prev = None
        # while root.val != p.val:
        #     if root.val > p.val:
        #         prev = root
        #         root = root.left
        #     elif root.val < p.val:
        #         root = root.right
        #     else:
        #         break
        # # Check if right child exists. If yes, go down and as furtherest left as possible.
        # # If not, return parent node
        # if not root.right:
        #     return prev
        # else:
        #     root = root.right
        #     while root.left:
        #         root = root.left
        #     return root
