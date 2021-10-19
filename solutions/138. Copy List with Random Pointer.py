"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
​
class Solution:
    def __init__(self):
            self.visitedHash = {}
    
    def copyRandomList(self, head: 'Node') -> 'Node':
        ## Soln 1 - Leetcode recursive w DFS
        if not head: return None
        
        if head in self.visitedHash:
            return self.visitedHash[head]
        node = Node(head.val, None, None)
        self.visitedHash[head] = node
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        return node
        
        ### Soln 0 - solution from Jake Reschke
        #if not head: return None
        #inp = head
        #inhead = inp
        #cp = Node(inp.val)
        #copyhead = cp
        #lib = {inp:cp, None:None}
        #while inp.next:
        #    inp = inp.next
