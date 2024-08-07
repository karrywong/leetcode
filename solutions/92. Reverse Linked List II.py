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
        prev = None
        cur = head
        while left > 1:
            prev = cur
            cur = cur.next
            left -= 1
            right -= 1
        
        tail, font = cur, prev # 2, 1
        while right > 0:
            cur.next, prev, cur = prev, cur, cur.next
            right -= 1
        
        # print(cur.val, prev.val) #5,4
        if font: 
            font.next = prev
        else:
            head = prev
        tail.next = cur
        
        return head
