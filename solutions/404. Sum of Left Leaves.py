# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        #DFS, time O(N), space O(N)
        ans = 0
        def helper(node, bo): #bo = True if left child, False otherwise
            nonlocal ans
            if node:
                if bo and not node.left and not node.right:
                    ans += node.val
                if node.left: helper(node.left, True)
                if node.right: helper(node.right, False)
        helper(root, False)     
        return ans
        
        # #BFS, time O(N), space O(N)
        # queue = collections.deque([(root, False)])
        # ans = 0
        # while queue:
        #     node, bo = queue.popleft()
        #     if bo and not node.left and not node.right:
        #         ans += node.val
        #     if node.left:
        #         queue.append((node.left, True))
        #     if node.right:
        #         queue.append((node.right, False))
        # return ans
