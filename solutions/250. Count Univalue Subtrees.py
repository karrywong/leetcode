# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        #Leetcode DFSby Stefan Pochmann, time O(N), space O(N)
        def helper(node, val) -> bool:
            if node is None:
                return True
            if not all([helper(node.left, node.val), helper(node.right, node.val)]):
                return False
            self.count += 1
            return node.val == val
        
        self.count = 0
        helper(root, 0)
        return self.count
    
#         #DFS, time O(N), space O(N)
#         if not root:
#             return 0
    
#         self.ans = 0
#         def helper(node) -> (bool, int): #bool, node value
#             if not node:
#                 return True, float('inf')
#             left_bo, left_val = helper(node.left)
#             right_bo, right_val = helper(node.right)
#             if left_bo and right_bo and left_val == right_val == float('inf'):
#                 self.ans += 1
#                 return True, node.val
#             elif left_bo and right_bo and ((left_val == float('inf') and node.val == right_val) or \
#                 (right_val == float('inf') and node.val == left_val) or left_val == node.val == right_val):
#                 self.ans += 1
#                 return True, node.val
#             else:
#                 return False, node.val
#         helper(root)
#         return self.ans
