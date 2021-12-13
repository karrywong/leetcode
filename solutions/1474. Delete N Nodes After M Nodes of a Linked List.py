# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        #First attempt, time: O(N), space: O(1)
        fast = head
        sentinel = ListNode(0,head)
        slow = sentinel
        while fast:
            i = 0
            while i < m and fast: 
                fast = fast.next
                slow = slow.next
                i += 1
            if not fast: break
            j = 0
            while j < n and fast:
                fast = fast.next
                j += 1
            if not fast:break
            slow.next = fast
        slow.next = None
        return sentinel.next
