# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        #Time complexity, O(N), Space O(N) - worst case: skewed tree
        #First to the node to be deleted and then from the node to be deleted to the leafs
        def getSuccessor(node): #once right, then left as far as possible
            node = node.right
            while node.left:
                node = node.left
            return node.val
            
        def getPredecessor(node): #once left, then right as far as possible
            node = node.left
            while node.right:
                node = node.right
            return node.val
        
        #driver code
        if not root:
            return root
        
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if (not root.left and not root.right):
                root = None
            elif root.right:
                root.val = getSuccessor(root)
                #recursively delete surccessor in the right subtree
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = getPredecessor(root)
                #recursively delete predecessor in the left subtree
                root.left = self.deleteNode(root.left, root.val)
        
        return root
