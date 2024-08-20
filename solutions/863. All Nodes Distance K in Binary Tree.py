from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
# suppose parent is given, can be access by node.parent
​
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # two-pass, time O(N), space O(N)
        def _dfs(node: TreeNode, parent_node:TreeNode=None) -> None:
            if not node:
                return
            lookup[node] = parent_node
            _dfs(node.left, node)
            _dfs(node.right, node)                
            return 
        
        ans = []
        lookup = {} #key:node, value: node's parent
        _dfs(root)
        
        dq = deque([(target,0)])
        visited = set() #memoization
        while dq:
            node, dist = dq.popleft()
            visited.add(node)
            if dist > k:
                break
            elif dist == k:
                ans.append(node.val)
            dist += 1
            
            # if node.parent: dq.append((node.parent,dist))
            ## suppose node's parent is not given
            for next_node in (node.left, node.right, lookup[node]):
                if next_node and next_node not in visited:
                    dq.append((next_node,dist))
            
        return ans
