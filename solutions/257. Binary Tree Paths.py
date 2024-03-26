# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
#         # backtrack v2, time O(N), space O(N)
#         ans = []
#         def dfs(node:Optional[TreeNode], lst:List[str]) -> None:
#             if node.left is None and node.right is None:
#                 ans.append("->".join(lst))
#                 return
            
#             if node.left:
#                 lst.append(str(node.left.val))
#                 dfs(node.left, lst)
#                 lst.pop()
#             if node.right:
#                 lst.append(str(node.right.val))
#                 dfs(node.right, lst)
#                 lst.pop()
#             return
#         dfs(root, [str(root.val)])
#         return ans
​
        #backtrack v1, time O(N), space O(N)
        ans = []
        def backtrack(node:Optional[TreeNode], lst:List[str]=[]) -> None:
            if node is None:
                return
            
            lst.append(str(node.val))
            if node.left is None and node.right is None:
                ans.append("->".join(lst))
            if node.left:
                backtrack(node.left, lst)
            if node.right:
                backtrack(node.right, lst)
            lst.pop()
            
        backtrack(root)
        return ans
​
        # #rimpoche 4-liner
        # if not root: return []
        # if not root.left and not root.right: return [str(root.val)]
        # return [str(root.val) + '->' + i for i in self.binaryTreePaths(root.left)] + \
        #     [str(root.val) + '->' + i for i in self.binaryTreePaths(root.right)]
