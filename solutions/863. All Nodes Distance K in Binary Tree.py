# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        #LeetCode Annotate Parent - use DFS to keep track of parent and BFS to compute distance
        #Time O(N), space O(N)
        parent = {}
        def dfs(node, par = None):
            if node:
                parent[node] = par
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)
​
        ans = []
        queue = collections.deque([(target, 0)])
        seen = set()
        while queue: #BFS
            node, dist = queue.popleft()
            seen.add(node)
            if dist == k:
                ans.append(node.val)
            
            for nei in (node.left, node.right, parent[node]):
                if nei and nei not in seen and dist < k:
                    queue.append((nei, dist+1))
        return ans
