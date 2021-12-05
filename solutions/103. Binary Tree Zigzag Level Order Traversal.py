# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #My DFS inspired by Leetcode DFS, clever, initialize ans a global array
        if not root: return root
        ans = collections.defaultdict(list)
        def dfs(node, level):
            if level % 2 == 0:
                ans[level].append(node.val)
            else:
                ans[level].insert(0,node.val)
            
            if node.left: dfs(node.left, level+1)
            if node.right: dfs(node.right, level+1)
        dfs(root, 0)
        return list(ans.values())
    
#         #LeetCode DFS
#         if not root: return root
#         ans = []
#         def dfs(node, level):
#             if level >= len(ans):
#                 ans.append(collections.deque([node.val]))
#             else:
#                 if level % 2 == 0:
#                     ans[level].append(node.val)
#                 else:
#                     ans[level].appendleft(node.val)
            
#             if node.left: dfs(node.left, level+1)
#             if node.right: dfs(node.right, level+1)
#         dfs(root, 0)
#         return ans
        
#         #First attempt, BFS, level size measurement
#         #True: left to right, False reversed
#         #Time O(N), Space O(N)
#         if not root: return root
#         queue = collections.deque([root])
#         bo = True
#         ans = []
        
#         while queue:
#             size = len(queue)
#             A = []
#             for i in range(size):
#                 node = queue.popleft()
#                 A.append(node.val)
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#             if bo:
#                 ans.append(A)
#             else:
#                 ans.append(reversed(A))
#             bo = not bo
#         return ans 
