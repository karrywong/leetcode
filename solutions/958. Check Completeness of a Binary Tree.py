# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:  
        #Soln 2 - soln by lee215, smart
        bfs = [root]
        i = 0
        while bfs[i]:
            bfs.append(bfs[i].left)
            bfs.append(bfs[i].right)
            i += 1
        return not any(bfs[i:])
        
#         #Soln 1 - my original idea
#         queue = collections.deque([root])
#         target = 1
#         while queue:
#             size = len(queue)
#             bo_end = False #denote end of level
#             for _ in range(size):
#                 node = queue.popleft()
            
#                 if bo_end and (node.left or node.right):
#                     return False
​
#                 if node.left and node.right:
#                     queue.append(node.left)
#                     queue.append(node.right)
#                 elif not node.left and node.right:
#                     return False
#                 else:  #(node.left and not node.right), (not node.left, not node.right)
#                     if node.left: queue.append(node.left)
#                     bo_end = True
            
#             if size != target and queue:
#                 return False
#             target *= 2
#         return True
