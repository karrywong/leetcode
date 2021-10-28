# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # second attempt by Jake
        if k == 1: return head
        scan = head
        new_head = None
        old_tail = None
        stack = []
        while True:
            if len(stack) < k:
                stack.append(scan)
            else:
                last = stack.pop()
                last.next = stack[-1]
                if not new_head:
                    new_head = last
                else:
                    old_tail.next = last
                for _ in range(k - 2):
                    last = stack.pop()
                    last.next = stack[-1]
                last = stack.pop()
                last.next = scan
                old_tail = last
                stack.append(scan)
            if scan:
