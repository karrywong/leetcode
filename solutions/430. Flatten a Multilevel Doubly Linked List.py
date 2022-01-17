"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
​
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #Leetcode DFS - recursion, time O(N), space O(N)
        if not head:
            return head
        sentinel = Node(None, None, head, None) # sentinel to ensure the `prev` pointer is never none
        self.dfs(sentinel, head)
        sentinel.next.prev = None #detach the sentinel from the real head
        return sentinel.next
    
    def dfs(self, prev, curr): #return the tail of the flatten list
        if not curr:
            return prev
        
        curr.prev = prev
        prev.next = curr
        
        temp = curr.next
        tail = self.dfs(curr, curr.child)
        curr.child = None
        return self.dfs(tail, temp)
        
#         #Jake's first attempt using recursion, time O(N), space O(N)
#         if not head: return head
        
#         def helper(node):
#             head = node
#             scan = node
#             while True:
#                 if scan.child:
#                     child_head, child_tail = helper(scan.child)
#                     next_node = scan.next
#                     scan.child, scan.next, child_head.prev = None, child_head, scan
#                     if next_node:
#                         next_node.prev, child_tail.next = child_tail, next_node
#                     scan = child_tail    
