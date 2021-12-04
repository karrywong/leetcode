# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        # #soln 2 - Leetcode recursion, time O(N), space O(N)
        # if not head or not head.next:
        #     return head
        # p = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return p 
        
        #soln 3 - more elegant in Python
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next   
        return prev
    
        # #soln 1 - one pass, time O(N), space O(1)
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
        # while head:
        #     stack.append(head.val)
        #     head = head.next
        # ans_ptr = ListNode(stack.pop())
        # ans = ans_ptr
        # while stack:
        #     ans_ptr.next = ListNode(stack.pop())
        #     ans_ptr = ans_ptr.next
        # return ans
