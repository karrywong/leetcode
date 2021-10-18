# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # soln 1 - both Karry and Jake
        if x == root.val or y == root.val: return False
        queue = collections.deque()
        depth = 0
        queue.append((root, depth, None))
        seen = {}
        
        while queue:
            node, depth, parent = queue.popleft()
            if node.val == x or node.val == y:
                seen[node.val] = (depth, parent)
                if len(seen.keys()) == 2:
                    return seen[x][0] == seen[y][0] and seen[x][1] != seen[y][1]
            if node.left: 
                queue.append((node.left, depth+1, node.val))
            if node.right:
                queue.append((node.right, depth+1, node.val))
            
