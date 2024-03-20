# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
#         # DFS, time O(N^2), space O(N)
#         ans = []
#         def dfs(node: Optional[TreeNode], remain_sum: int, path: List[int]=[]) -> None:
#             if node is None:
#                 return
                
#             path.append(node.val)
#             if node.left is None and node.right is None and node.val == remain_sum:
#                 ans.append(path[:])
#             else:
#                 dfs(node.left, remain_sum-node.val, path)
#                 dfs(node.right, remain_sum-node.val, path)
#             path.pop()
        
#         dfs(root, targetSum)
#         return ans
​
        #soln 0 - first attempt, backtracking
        ans = []
        def backtrack(node, val, lst):
            if node.left is None and node.right is None and val == targetSum:
                ans.append(lst[:])
                return
​
            if node.left:
                lst.append(node.left.val)
                backtrack(node.left, val+node.left.val, lst)
                lst.pop()
            if node.right:
                lst.append(node.right.val)
                backtrack(node.right, val+node.right.val, lst)
                lst.pop()
        if not root: return ans
        backtrack(root, root.val, [root.val])
        return ans
