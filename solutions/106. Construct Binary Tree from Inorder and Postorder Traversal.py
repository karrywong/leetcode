# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        def helper(left:int=0, right:int=n-1) -> Optional[TreeNode]:
            if left > right:
                return None
            val = postorder[self.postorder_ind]
            node = TreeNode(val)
            self.postorder_ind -= 1
​
            node.right = helper(lookup[val]+1, right)
            node.left = helper(left, lookup[val]-1)
            return node
        
        lookup = {val:idx for idx, val in enumerate(inorder)}
        self.postorder_ind = n-1
        return helper()        
