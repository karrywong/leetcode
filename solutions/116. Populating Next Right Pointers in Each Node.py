"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
​
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        #soln 1 - Leetcode BFS
        if not root: return root
        queue = collections.deque([root])
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i < size - 1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                    queue.append(node.right)
        return root
        
        #soln 0 - first attempt with Jake Reschke
#         if not root: return root
#         queue = collections.deque([root])
#         n, count = 0, 1
        
#         while queue:
#             if (count == 2**n):
#                 prev, cur = None, queue.popleft()
#                 n += 1
#             else:
#                 prev, cur = cur, queue.popleft()
#             count += 1
                
#             cur.next = prev
#             if cur.right:
#                 queue.append(cur.right)
#                 queue.append(cur.left)
                
