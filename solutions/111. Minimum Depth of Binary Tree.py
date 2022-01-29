# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        #LeetCode BFS:
        if not root: return 0
        queue = collections.deque([(root,1)])
        while queue:
            node, depth = queue.popleft()
            children = [node.left, node.right]
            if not any(children):
                return depth
            for c in children:
                if c:
                    queue.append((c,depth+1))
                
        # #LeetCode DFS, cleaner, time O(N), space O(N)
        # if not root: return 0
        # children = [root.left, root.right]
        # if not any(children):
        #     return 1
        # return min([self.minDepth(c) for c in children if c]) + 1
        
        # #First attempt, DFS, time O(N), space O(N) due to recursion
        # if not root:
        #     return 0
        # elif not root.left and not root.right:
        #     return 1
        # elif root.left and not root.right:
        #     return self.minDepth(root.left) + 1
        # elif not root.left and root.right:
        #     return self.minDepth(root.right) + 1
        # else:
        #     return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
