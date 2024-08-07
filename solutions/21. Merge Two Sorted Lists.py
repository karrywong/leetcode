# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         # Time O(n+m), n=len(l1), m=len(l2), space O(n+m)
#         ans = ListNode(None)
#         cur = ans
        
#         while l1 and l2:
#             if l1.val <= l2.val:
#                 cur.next  = ListNode(l1.val)
#                 l1 = l1.next
#             else:
#                 cur.next  = ListNode(l2.val)
#                 l2 = l2.next
#             cur = cur.next
            
#         cur.next = l1 if l1 else l2
#         return ans.next 
    
        # Leetcode, recursion, time O(n+m), space O(n+m)
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
