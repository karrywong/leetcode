# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        #soln 1 - Leetcode w sentinel node, Time O(N), Space O(1)
        sentinel = ListNode(0)
        sentinel.next = head
        sentinel_ptr, head_ptr = sentinel, head
        while head_ptr:
            if head_ptr.val != val:
                sentinel_ptr = head_ptr
            else:
                sentinel_ptr.next = head_ptr.next
            head_ptr = head_ptr.next
        return sentinel.next
        
        # #soln 0 - first attempt, Time O(N), Space O(N)
        # ans_ptr = ListNode(None)
        # ans = ans_ptr
        # while head:
        #     if head.val != val:
        #         ans_ptr.next = ListNode(head.val)
        #         ans_ptr = ans_ptr.next
        #     head = head.next
        # return ans.next   
