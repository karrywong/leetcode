# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
#         #Leetcode recursion + backtracking, time O(N), space O(1)
#         left_ptr, right_ptr = head, head
#         stop = False
#         def recurse(right_ptr, left, right):
#             nonlocal left_ptr, stop
#             if right == 1: #base case
#                 return
#             right_ptr = right_ptr.next
            
#             if left > 1: 
#                 left_ptr = left_ptr.next
#             recurse(right_ptr, left-1, right-1)
            
#             if left_ptr == right_ptr or right_ptr.next == left_ptr:
#                 stop = True
            
#             if not stop:
#                 left_ptr.val, right_ptr.val = right_ptr.val, left_ptr.val
#                 left_ptr = left_ptr.next
#         recurse(right_ptr, left, right)
#         return head
        
        #Leetcode iterative reversal, slight more difficult than 206. Reverse Linked List
        #Time O(N), space O(1)
        cur, prev = head, None
        while left > 1:
            prev = cur
            cur = cur.next
            left, right = left-1, right-1
        
        tail, start = cur, prev
        # print(tail.val, start.val)
        while right:
            cur.next, prev, cur = prev, cur, cur.next
            right -= 1
        
        if start:
            start.next = prev
        else:
            head = prev
        tail.next = cur
        return head
        
#         #First attempt, time O(N), space O(N)
#         if left == right:
#             return head
        
#         ptr = head
#         sentinel = ListNode(0, head)
#         ptr1 = sentinel
#         for i in range(left-1):
#             ptr = ptr.next
#             ptr1 = ptr1.next
        
#         stack = []
#         for i in range(right-left+1):
#             stack.append(ptr)
#             ptr = ptr.next
        
#         prev = stack.pop()
#         ptr1.next = prev
#         while stack:
#             prev.next = stack.pop()
#             prev = prev.next
#         prev.next = ptr
        
#         return sentinel.next
