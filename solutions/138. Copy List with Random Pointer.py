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
        inhead = inp = head             # input head, input pointer
        copyhead = cp = Node(inp.val)   # copy head, copy pointer
        lib = {inp : copyhead, None : None } # initalize mapping
        while inp.next:                 # first make copy of linked list, ignore random
            inp = inp.next
            cp.next = Node(inp.val)
            cp = cp.next
            lib[inp] = cp       # build mapping between nodes
        cp = copyhead          # reset copy pointer to head for second loop through
        while head:             # can change head now, won't need reference to input head
            cp.random = lib[head.random]    # set cp.random using the map
            head = head.next
            cp = cp.next
        return copyhead
​
