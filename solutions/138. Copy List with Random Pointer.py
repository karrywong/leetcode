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
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        ### Soln 0 - solution from Jake Reschke
        if not head:
            return None
         
        inp = head #input pointer
        #inhead = inp # input head
        cp = Node(inp.val) #copy pointer
        copyhead = cp #copy head 
        lib = {inp : copyhead, None : None } # initalize mapping
        
        # first make copy of linked list, ignore random
        while inp.next:                 
            inp = inp.next
            cp.next = Node(inp.val)
            cp = cp.next
            lib[inp] = cp       # build mapping between nodes
        
        cp = copyhead          # reset copy pointer to head for second loop through
        while head:             # can change head now, won't need reference to input head
            cp.random = lib[head.random]    # set cp.random using the map
            head = head.next
            cp = cp.next
​
        return copyhead
