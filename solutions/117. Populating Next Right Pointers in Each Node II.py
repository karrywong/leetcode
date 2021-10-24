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
        
        nodeQ = collections.deque([(root,0)]) # (root,level) pair
        
        while nodeQ:
            cur,cur_level = nodeQ.popleft()
            if nodeQ and nodeQ[0][1] == cur_level:
                cur.next = nodeQ[0][0]
            else:
                cur.next = None
            
            if cur.left:
                nodeQ.append((cur.left,cur_level + 1))
            if cur.right:
                nodeQ.append((cur.right,cur_level + 1))
                
        return root
        
