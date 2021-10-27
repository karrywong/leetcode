# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        scan = head
        for _ in range(k - 1):
            scan = scan.next
        first = scan
        second = head
        while scan.next:
            scan = scan.next
            second = second.next
        second.val,first.val = first.val,second.val
        
        return head
