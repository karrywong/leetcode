# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # val = 0
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             Solution.val = 0
#             return 0
        
#         lres = self.equalToDescendants(root.left)
#         lval = Solution.val
#         rres = self.equalToDescendants(root.right)
#         rval = Solution.val
#         Solution.val = lval + root.val + rval
        
#         return (root.val == lval+rval) + lres + rres
        
        #Time O(N), N is number of nodes, space O(N)
        count = 0
        def helper(node: TreeNode) -> int: #DFS
            nonlocal count
            if not node:
                return 0
            
            lval = helper(node.left)
            rval = helper(node.right)
            
            if node.val == lval+rval:
                count += 1
            
            return node.val+lval+rval
        helper(root)
        return count
