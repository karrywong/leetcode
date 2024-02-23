# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Recursion 1
        # if not root: 
        #     return []
        # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)        
        
        # Recursion 2
        res = []
        def helper(node: Optional[TreeNode]) -> None:
            if node is not None:
                helper(node.left)
                res.append(node.val)
                helper(node.right)
                
        helper(root)
        return res
        
        # #Iterative - version 1
        # node = root
        # stack, ans = [], []
        # while stack or node :
        #     while node is not None:
        #         stack.append(node)
        #         node = node.left
        #     node = stack.pop()
        #     ans.append(node.val)
        #     node = node.right
        # return ans
        
        # # Iterative - version 2
        # node = root
        # stack, ans = [], []
        # while True:
        #     if node is not None:
        #         stack.append(node)
        #         node = node.left 
        #     elif len(stack) > 0:
        #         node = stack.pop()
        #         ans.append(node.val)
        #         node = node.right
        #     else:
        #         break
        # return ans
