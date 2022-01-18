# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
#         #LeetCode's preorder DFS, time O(N), space O(N)
#         def dfs(curr_node, depth):
#             nonlocal u_depth, ans
#             if curr_node == u:
#                 u_depth = depth
#                 return
            
#             if depth == u_depth:
#                 if ans is None:
#                     ans = curr_node
            
#             if curr_node.left:
#                 dfs(curr_node.left, depth+1)
#             if curr_node.right:
#                 dfs(curr_node.right, depth+1)
        
#         u_depth, ans = -1, None
#         dfs(root, 0)
#         return ans
    
        #LeetCode's use of sentinel node, time O(N), space O(N)
        queue = collections.deque([root, None])
        while queue:
            curr = queue.popleft()
            if curr == u:
                return queue.popleft()
            
            if curr:
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            else:
                if queue:
                    queue.append(None)
        
        # #First attempt similar to LeetCode soln, time O(N), space O(N)
        # queue = collections.deque([root])
        # while queue:
        #     level_size = len(queue)
        #     for i in range(level_size):
        #         node = queue.popleft()
        #         if node == u:
        #             return queue[0] if i != level_size-1 else None
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
