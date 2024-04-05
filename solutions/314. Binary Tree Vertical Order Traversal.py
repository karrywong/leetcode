# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         # Leetcode soln 2, time O(N), space O(N)
#         if root is None:
#             return []
        
#         max_col = min_col = 0
#         column_lookup = defaultdict(list)
#         queue = deque([(root,0)])
        
#         while queue:
#             node, col = queue.popleft()
#             if node is not None:
#                 max_col = max(max_col, col)
#                 min_col = min(min_col, col)
#                 column_lookup[col].append(node.val)
                
#                 queue.append((node.left, col-1))
#                 queue.append((node.right, col+1))
                
#         return [column_lookup[k] for k in range(min_col, max_col+1)]      
        
#         # Leetcode soln 1, time O(NlogN), space O(N)
        column_lookup = defaultdict(list)
        queue = deque([(root,0)])
        
        while queue:
            node, col = queue.popleft()
            if node is not None:
                column_lookup[col].append(node.val)
                
                queue.append((node.left, col-1))
                queue.append((node.right, col+1))
                
        return [column_lookup[k] for k in sorted(column_lookup.keys())]
    
    
