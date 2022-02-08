"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
​
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        #Recursion, time O(N), space O(N)
        ans = []
        if not root:
            return root
        
        def helper(node, level):
            if len(ans) == level:
                ans.append([])
            ans[level].append(node.val)
            
            for child in node.children:
                helper(child, level+1)
        helper(root, 0)
        return ans
        
#         #LeetCode simplified BFS, time O(N), space O(N)
#         #w/o for-loop range(len(queue))
#         if not root: return root
#         ans = []
#         prev_layer = [root]
        
#         while prev_layer:
#             cur_layer = []
#             ans.append([])
#             for node in prev_layer:
#                 ans[-1].append(node.val)
#                 cur_layer.extend(node.children)
#             prev_layer = cur_layer
#         return ans
        
