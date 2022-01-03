# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        #Direct computation or Bit manipulation, time O(N), space O(1)
        ptr = head
        ans = 0
        while ptr:
            # ans *= 2 
            # ans += ptr.val
            ans <<= 1
            ans |= ptr.val
            ptr = ptr.next
        return ans
