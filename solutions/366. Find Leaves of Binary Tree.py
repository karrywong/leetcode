# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
    # optimal solution, DFS, solution on the fly, idea from jz2966
    #Time complexity O(N) where N is the total number of nodes, Space O(N), ie return all nodes
        self.ans = collections.defaultdict(list)
        def dfs(node, depth=0):
            if not node:
                return depth
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            cur_depth = max(left_depth, right_depth)
            self.ans[cur_depth].append(node.val)
            return cur_depth + 1 #compute BT depth - max(left_subtree_depth, right_subtree_depth)+1
        dfs(root)
        return self.ans.values() #list of list
    
#     #First attempt, real mock interview practice, solution given within 25 minutes
#     def helper(self, node): #Recursion, input tree, output tree without leaf nodes
#         if node: 
#             if node.left is None and node.right is None: #leaf node
#                 self.leaf.append(node.val)
#                 return True
#             if self.helper(node.left): 
#                 node.left = None    
#             if self.helper(node.right):
#                 node.right = None
#             return False
​
#     def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
#         #Time complexity O(H^2) where H is the depth of input BT root
#         #Worst case: O(N^2) where N is the number of node in a skew tree
#         self.ans = []
        
#         while root:
#             self.leaf = []
#             bo = self.helper(root)
#             if bo: root = None
#             self.ans.append(self.leaf)
#         return self.ans
