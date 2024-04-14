"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""
​
class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        # headd is empty list
        if head is None:
            node = Node(val=insertVal)
            node.next = node
            return node
        
        prev, cur = head, head.next
        
        while True:
            if prev.val <= insertVal <= cur.val:
                break
            elif prev.val > cur.val:
                if prev.val < insertVal or cur.val > insertVal:
                    break
            
            prev, cur = cur, cur.next
            if prev == head:
                break
            
        prev.next = Node(insertVal, cur)
        return head
            
