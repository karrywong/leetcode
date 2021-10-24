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
        if not root: return root
        queue = collections.deque()
        queue.append(root) #1
        n, count = 0, 1
        
        while queue:
            if (count == 2**n):
                prev, cur = None, queue.popleft()
                n += 1
            else:
                prev, cur = cur, queue.popleft()
            count += 1
                
            cur.next = prev
            if cur.right:
                queue.append(cur.right)
                queue.append(cur.left)
                
        return root
            
        
​
