# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        # iterative, time O(N), space O(1)
        prev = None
        cur = head
        while cur:
            # temp = cur.next
            # cur.next = prev
            # prev = cur
            # cur = temp
            cur.next, prev, cur = prev, cur, cur.next # one-step 
        return prev
    
        # # recursion, time O(N), space O(N)
        # if head is None or head.next is None:
        #     return head
        # cur = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return cur
    
        # # stack, time O(N), space O(N)
        # stack = []
        # cur = head
        # while cur:
        #     stack.append(cur)
        #     cur = cur.next
        # ans = ListNode(None)
        # cur = ans
        # while stack:
        #     cur.next = stack.pop()
        #     cur = cur.next
        # cur.next = None
        # return ans.next
