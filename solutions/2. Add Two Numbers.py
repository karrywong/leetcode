# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # time O(N), space O(N)
        ans = ListNode(0)
        cur = ans
        carry = 0
        while l1 or l2:
            if l1:
                x = l1.val 
                l1 = l1.next 
            else:
                x = 0
                
            if l2:
                y = l2.val
                l2 = l2.next
            else:
                y = 0
            total = x + y + carry
            carry, val = divmod(total, 10)
            cur.next = ListNode(val)
            cur = cur.next
        if carry:
            cur.next = ListNode(carry)
        return ans.next
    
        # naive
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
        
        #n, r = divmod(n, 10)
        #ans = ListNode(r)
        #ans_tail = ans
        #while n > 0:
        #    n, r = divmod(n, 10)
        #    ans_tail.next = ListNode(r)
        #    ans_tail = ans_tail.next
        #return ans
            
