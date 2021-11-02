# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #soln 1 - Leetcode smart
        curr = head
        while curr and curr.next:
            if curr.next.val == curr.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
        
        # #soln 0 - naive attempt, one-pass
        # if not head: return head
        # ans_ptr = ListNode(head.val)
        # ans = ans_ptr
        # head = head.next
        # while head:
        #     if head.val == ans_ptr.val:
        #         head = head.next
        #     else:
        #         ans_ptr.next = ListNode(head.val)
        #         ans_ptr = ans_ptr.next
        # return ans
