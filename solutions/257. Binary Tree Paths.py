# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
#         #First attempt, time O(N), space O(N)
#         ans = []
#         def backtrack(node, path=[]):
#             if node:
#                 path.append(str(node.val))
#                 if node.left is None and node.right is None:
#                     ans.append("->".join(path[:]))
                
#                 if node.left:
#                     backtrack(node.left, path)
                
#                 if node.right:
#                     backtrack(node.right, path)
                
#                 path.pop()
        
#         backtrack(root)
#         return ans
​
        #rimpoche 4-liner
        if not root: return []
        if not root.left and not root.right: return [str(root.val)]
        return [str(root.val) + '->' + i for i in self.binaryTreePaths(root.left)] + \
            [str(root.val) + '->' + i for i in self.binaryTreePaths(root.right)]
