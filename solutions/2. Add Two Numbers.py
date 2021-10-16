# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #Leetcode soln 1
        dummyhead = ListNode(0)
        curr = dummyhead
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sval = carry + x + y
            carry, r = divmod(sval, 10)
            curr.next = ListNode(r)
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
                
        if carry > 0: curr.next = ListNode(carry)
        return dummyhead.next
            
        #my solution
        #n = 0
        #i = 0
        #while l1 or l2:
        #    if l1: 
        #        n += l1.val * 10**i 
        #        l1 = l1.next
        #    if l2:
        #        n += l2.val * 10**i
        #        l2 = l2.next
        #    i += 1
        
