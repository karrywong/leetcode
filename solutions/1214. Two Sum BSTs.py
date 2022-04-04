# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        #First attempt, time O(max(N1, N2)) where N1 = size(root1) and N2 = size(root2), space O(N1)
        def inorder(node: TreeNode) -> List[int]:
            if not node: return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        def findComplement(node: TreeNode, complement: int) -> bool:
            while node:
                if node.val == complement:
                    return True
                elif node.val < complement:
                    node = node.right
                else:
                    node = node.left
            return False
        
#         lst1 = inorder(root1)
#         for x in lst1:
#             if findComplement(root2, target-x):
#                 return True
#         return False
            
#         ### old attempt - record complement for root1 in a hashtable and search through root2
#         self.lib = {}
#         def dfs(node, k):
#             if node:
#                 self.lib[k - node.val] = node.val
#                 dfs(node.left, k)
#                 dfs(node.right, k)
#         dfs(root1, target)
        
#         def valid(node,k):
#             if node:
#                 if node.val in self.lib:
#                     return True
