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
    def copyRandomList(self, head):
        
        ### Soln 0 - first attempt, idea from Jake Reschke
        if not head:
            return None
        inhead = inp = head
        copyhead = inc = Node(inp.val)
        lib = {inp : copyhead, None : None }
        while inp.next:
            inp = inp.next
            inc.next = Node(inp.val)
            inc = inc.next
            lib[inp] = inc
        inc = copyhead
        while head:
            inc.random = lib[head.random]
            head = head.next
            inc = inc.next
        return copyhead
