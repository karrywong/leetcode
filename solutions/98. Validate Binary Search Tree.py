# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode], min_val: float = float('-inf'), max_val: float = float('inf')) -> bool:
#         # self-attempt, DFS bottom-up, time O(N), space O(N)
#         def dfs(root: Optional[TreeNode]) -> Tuple[bool, int, int]:
#             if root is None:
#                 return True, float('inf'), float('-inf')
            
#             left_bool, left_min, left_max = dfs(root.left)
#             right_bool, right_min, right_max = dfs(root.right)
            
#             if not left_bool or not right_bool or root.val <= left_max or root.val >= right_min:
#                 return False, float('inf'), float('-inf')
#             return True, min(left_min,right_min,root.val), max(left_max,right_max,root.val)
        
#         return dfs(root)[0]
        
        #soln 2 - Recursive Inorder Traversal, time O(N), space O(N)
        self.prev_val:float=float('-inf')
        def dfs(node: Optional[TreeNode]) -> bool:
            if not node:
                return True
            if not dfs(node.left):
                return False
            if node.val <= self.prev_val:
                return False
            self.prev_val = node.val
            return dfs(node.right)
        return dfs(root)
        
        # #soln 1 - Recursive Traversal with Valid Range, time O(N), space O(N)
        # def validate(node, low=float('-inf'), high=float('inf')):
        #     if not node:
        #         return True
        #     if node.val <= low or node.val >= high:
        #         return False
        #     return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        # return validate(root)
        
#         # #soln 0 - standard inorder traversal, slow
#         def helper(node):
#             if not node:
#                 return []
#             return helper(node.left) + [node.val] + helper(node.right)
#         lst = helper(root)
#         return all([lst[i] < lst[i+1] for i in range(len(lst)-1)])
            
