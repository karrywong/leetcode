"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: Optional['Node']) -> Optional['Node']:
        #Leetcode DFS - recursion, time O(N), space O(N)
        if head is None:
            return None
        sentinel = Node()
        sentinel.next = head
        self.dfs(prev=sentinel, curr=head)
        head.prev = None
        return sentinel.next
    
    def dfs(self, prev: Optional['Node'], curr: Optional['Node']) -> Optional['Node']: #return the tail of the flatten list
        if curr is None:
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
                    
#                 if not scan.next: 
#                     tail = scan
#                     break
#                 scan = scan.next        
#             return head, tail
        
#         head, _ = helper(head)
#         return head
