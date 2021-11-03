# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #soln 0 - naive attempt, two pass
        if not head: return head
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        stack.sort(reverse=True)
        ans_ptr = ListNode(stack.pop())
        ans = ans_ptr
        while stack:
            ans_ptr.next = ListNode(stack.pop())
            ans_ptr = ans_ptr.next
        return ans
        
