# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # time O(N), space O(N)
        # create monotonic queue, non-increasing        
        # [5,2,13,3,8]
        #           |
        # queue = [13,8]
        
        queue = []
        cur = head
        while cur:
            while queue and queue[-1].val < cur.val:
                queue.pop()
            queue.append(cur)
            cur = cur.next
        
        sentinel_node = ListNode(0)
        cur = sentinel_node
        for node in queue:
            cur.next = node
            cur = cur.next
        return sentinel_node.next
        
