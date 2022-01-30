# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        #Failed attempts, tricky, refer to a similar but simpler problem, 979. Distribute Coins in Binary Tree
        #LeetCode soln 2 - Greedy w/ key ideas:
        #scene I - a node has its children covered and has a parent, then it is strictly better to place the camera at this node's parent.
        #scene II - a node has children that are not covered by a camera, then we must place a camera here
        #scene III - a node has no parent and it is not covered, we must place a camera here.
        self.ans = 0
        covered = {None}
        
        def dfs(node, parent = None):
            if not node:
                return 
            dfs(node.left, node)
            dfs(node.right, node)
            
            if (parent is None and node not in covered) or node.left not in covered or node.right not in covered:
                self.ans += 1
                covered.update({node, parent, node.left, node.right})
                
        dfs(root)
        return self.ans 
        
        #LeetCode soln 1 - DP
        # 0: Strict ST; All nodes below this are covered, but not this one -> node's children must be in state 1
        # 1: Normal ST; All nodes below and incl this are covered - no camera -> node's children either 1 or 2, at least one child is in 2 
        # 2: Placed camera; All nodes below this are covered, plus camera here      
#         def dfs(node) -> (int,int,int): #count for cases 0, 1, 2
#             if not node:
#                 return 0,0,float('inf')
            
#             left = dfs(node.left)
#             right = dfs(node.right)
            
#             dp0 = left[1] + right[1] #case 0
#             dp1 = min(min(left[1:])+right[2], min(right[1:])+left[2])
#             dp2 = 1 + min(left) + min(right)
#             return dp0, dp1, dp2
        
#         return min(dfs(root)[1:])
