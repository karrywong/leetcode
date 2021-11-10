# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #soln 2 - Leetcode Floyd's algorithm
        if head is None: return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
        
        # #soln 1 - Leetcode Hashtable 
        # nodes_seen = set()
        # while head:
        #     if head in nodes_seen:
        #         return True
        #     nodes_seen.add(head)
        #     head = head.next
        # return False
        
#         #soln 0 - first attempt
#         if not head or not head.next: 
#             return False
