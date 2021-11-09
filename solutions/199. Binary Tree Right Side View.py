# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #soln 1 - Leetcode BFS with sentinel node
        if not root: return root
        ans, queue = [], collections.deque([root, None])
        curr = root 
        while queue:
            prev, curr = curr, queue.popleft()
            
            while curr:
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                prev, curr = curr, queue.popleft()
            # the current level is finished, curr = None, prev = rightmost element
            ans.append(prev.val)
            if queue: #add sentinel
                queue.append(None)
        return ans
        
        #soln 0 - first attempt, BFS
        # if not root: return root
        # ans, queue = [], collections.deque([root])
        # while queue:
        #     size = len(queue)
        #     for i in range(size):
        #         node = queue.popleft()
        #         if i == size - 1:
        #             ans.append(node.val)
        #         if node.left:
