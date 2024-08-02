# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # one-pass, Time: O(N), Space O(1)
        slow = fast = head
        count = 0
        while fast and count < n:
            fast = fast.next
            count += 1
        
        sentinel = ListNode(0)
        sentinel.next = head
        ans_ptr = sentinel 
        while fast:
            ans_ptr = ans_ptr.next
            fast = fast.next
            slow = slow.next
        
        ans_ptr.next = slow.next
        return sentinel.next
​
#         # two-pass, Time: O(N), Space O(1
#         cnt = 0
#         cur = head
#         while cur:
#             cnt += 1
#             cur = cur.next
        
#         cnt -= n
#         sentinel = ListNode(0, head)
#         ptr = sentinel
#         while cnt > 0:
#             ptr = ptr.next
#             cnt -= 1
#         ptr.next = ptr.next.next
#         return sentinel.next
    
