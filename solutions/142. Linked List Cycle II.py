# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        #soln 2 - Leetcode Floyd's algorithm
        slow = head
        fast = head
        while True:
            if fast is None or fast.next is None:
                return None
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        
        head_ptr = head
        while head_ptr != fast:
            head_ptr = head_ptr.next
            fast = fast.next
        return fast
        
        # #soln 1 - Hashtable, same as 141. Linked List Cycle
        # nodes_seen = set()
        # head_ptr = head
        # while head_ptr:
        #     if head_ptr in nodes_seen:
        #         return head_ptr
        #     nodes_seen.add(head_ptr)
        #     head_ptr = head_ptr.next
        # return None
