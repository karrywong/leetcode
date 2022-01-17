# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
#         #DFS solution, inspired by Zitao Wang in discussion
#         #Time O(N), space O(N)
#         seen = set()
#         def dfs(node):
#             if not node or (node.right and node.right.val in seen):
#                 return None
            
#             seen.add(node.val)
#             if node.right:
#                 node.right = dfs(node.right)
#             if node.left:
#                 node.left = dfs(node.left)
#             return node
#         return dfs(root)
    
        #BFS solution, inspired by Zitao Wang in discussion
        #Time O(N), space O(N)
        queue = collections.deque([root])
        seen = set([root.val])
        while queue:
            node = queue.popleft()
            if node.right:
                if node.right.right and node.right.right.val in seen:
                    node.right = None
                    return root
                seen.add(node.right.val)
                queue.append(node.right)
            if node.left:
                if node.left.right and node.left.right.val in seen:
                    node.left = None
                    return root
                seen.add(node.left.val)
                queue.append(node.left)
