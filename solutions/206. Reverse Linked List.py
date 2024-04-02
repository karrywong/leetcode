# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: 
#         if (not head) or (not head.next):
#             return head
#         cur = self.reverseList(head.next)
#         head.next.next = head
#         head.next = None
#         return cur
    
#         # soln 2 - more elegant
#         prev, cur = None, head
#         while cur:
#             cur.next, prev, cur = prev, cur, cur.next
#         return prev
        
#         # soln 1 - one pass, time O(N), space O(1)
#         prev = None
#         cur = head
#         while cur:
#             next_temp = cur.next
#             cur.next = prev
#             prev = cur
#             cur = next_temp
#         return prev
    
        # stack, time O(N), space O(N)
        stack = []
        cur = head 
        while cur:
            stack.append(cur)
            cur = cur.next
        if not stack: return None
        ans = stack.pop()
        cur = ans
        while stack:
            cur.next = stack.pop()
            cur = cur.next
        cur.next = None
        return ans
