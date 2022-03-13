# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Time O(N), N is length of linked list, space O(1)
        p1 = head
        if p1 is None or p1.next is None: 
            return p1
        p3 = p2 = head.next
        
        while p2 is not None and p2.next is not None:
            p1.next = p2.next
            p1 = p1.next
            p2.next = p1.next
            p2 = p2.next
        p1.next = p3
        
        return head
