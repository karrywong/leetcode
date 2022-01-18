# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #Recursion from Sacharya1 in discussion
    def __init__(self):
        self.myList = []
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            self.getLonelyNodes(root.left)
            self.getLonelyNodes(root.right)
            if root.left and not root.right:
                self.myList.append(root.left.val)
            elif not root.left and root.right:
                self.myList.append(root.right.val)
        return self.myList
        
#         #First attempt, time O(N), space O(N)
#         ans = []
#         def dfs(node):
#             if node is None:
#                 return
            
#             if (node.left and node.right is None) :
#                 ans.append(node.left.val)
#             elif (node.right and node.left is None):
#                 ans.append(node.right.val)
            
#             if node.left:
#                 dfs(node.left)
#             if node.right:
#                 dfs(node.right)
                
#         dfs(root)
#         return ans
