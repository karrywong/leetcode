# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        ### Soln 1 - First attempt
#         if t1 and t2:
#             answer = TreeNode(t1.val + t2.val)
#         elif not t1 and t2:
#             answer = TreeNode(t2.val)
#         elif t1 and not t2:
#             answer = TreeNode(t1.val)
#         else:
#             return None
            
#         answer.left = self.mergeTrees(t1.left if t1 else None, t2.left if t2 else None)
#         answer.right = self.mergeTrees(t1.right if t1 else None, t2.right if t2 else None)
        
#         return answer
​
        ### Soln 2 - improved
        if t1 and t2:
            answer = TreeNode(t1.val + t2.val)
            answer.left = self.mergeTrees(t1.left, t2.left)
            answer.right = self.mergeTrees(t1.right, t2.right)
        else:
            return t1 or t2
        return answer
            
