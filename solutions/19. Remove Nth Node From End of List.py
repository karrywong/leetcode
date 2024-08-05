# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # one-pass, Time: O(N), Space O(1)
        sentinel = ListNode(None)
        sentinel.next = head
        fast = sentinel
        while n >= 0 and fast:
            fast = fast.next
            n -= 1
        
        slow = sentinel
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
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
