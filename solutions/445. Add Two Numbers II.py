# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #Straightforward approach, first reverse input l1, l2, then add them and connect them in reversed order
        #Time O(N1+N2), w 
        def reverse_linklst(head: ListNode) -> ListNode:
            prev = None
            curr = head
            while curr:
                curr.next, prev, curr = prev, curr, curr.next
            return prev
        
        l1 = reverse_linklst(l1)                
        l2 = reverse_linklst(l2)
        
        head = None
        carry = 0
        while l1 or l2:
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry, r = divmod(val, 10)
            
            temp = ListNode(r)
            temp.next, head = head, temp
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        if carry:
            temp = ListNode(carry)
            temp.next, head = head, temp
        return head
