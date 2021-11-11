# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # soln 0 - first attempt, iteration, Time O(n+m), Space O(n+m)
        ans_ptr = ListNode(0)
        ans = ans_ptr
        l1_ptr, l2_ptr = l1, l2
        while l1_ptr and l2_ptr:
            if l1_ptr.val <= l2_ptr.val:
                ans_ptr.next = ListNode(l1_ptr.val)
                l1_ptr = l1_ptr.next
            else:    
                ans_ptr.next = ListNode(l2_ptr.val)
                l2_ptr = l2_ptr.next
            ans_ptr = ans_ptr.next
        
        if l1_ptr:
            ans_ptr.next = l1_ptr
        else:
            ans_ptr.next = l2_ptr
        return ans.next
    
        # # soln 1 - Leetcode recursion, Time O(n+m), Space O(n+m)
        # if l1 is None:
        #     return l2
        # elif l2 is None:
        #     return l1
        # elif l1.val < l2.val:
        #     l1.next = self.mergeTwoLists(l1.next, l2)
        #     return l1
        # else:
        #     l2.next = self.mergeTwoLists(l1, l2.next)
        #     return l2
            
        
