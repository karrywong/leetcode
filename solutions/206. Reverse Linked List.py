# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        #soln 2 - Leetcode recursion
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p 
        
        # #soln 1 - one pass
        # if not head: return head
        # prev = ListNode(head.val)
        # curr = head
        # curr = curr.next
        # while curr:
        #     next_temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = next_temp
        # return prev
        
        # #soln 0 - naive attempt, two pass
        # if not head: return head
        # stack = []
