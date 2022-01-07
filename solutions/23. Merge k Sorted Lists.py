# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #LeetCode Priority Queue, optimized from compare one-by-one
        ListNode.__eq__ = lambda self, other: self.val == other.val
        ListNode.__lt__ = lambda self, other: self.val < other.val
        
        nodes = []
        heapq.heapify(nodes)
        head = ListNode(None)
        ptr = head
        for lst in lists:
            if lst:
                heapq.heappush(nodes,(lst.val,lst))
        while nodes:
            val, node = heapq.heappop(nodes)
            ptr.next = ListNode(val)
            ptr = ptr.next
            node = node.next
            if node:
                heapq.heappush(nodes,(node.val, node))
        return head.next
            
        # #LeetCode brute force - collect all values and sort
        # #Time O(NlogN), space O(N)
        # nodes = []
        # head = ListNode(None)
        # ptr = head
        # for lst in lists:
        #     while lst:
        #         nodes.append(lst.val)
        #         lst = lst.next
        # for x in sorted(nodes):
        #     ptr.next = ListNode(x)
        #     ptr = ptr.next
        # return head.next
