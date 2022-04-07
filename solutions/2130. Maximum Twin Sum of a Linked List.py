# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        #Cut and reverse second half of linked list, time O(N), space O(1)
        def reverse(ptr):
            prev, cur = None, ptr
            while cur:
                cur.next, prev, cur = prev, cur, cur.next
            return prev
        
        prev = None
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            prev, slow = slow, slow.next
        prev.next = None
        head_reversed = reverse(slow)
        maxval = float('-inf')
        while head and head_reversed:
            maxval = max(maxval, head.val + head_reversed.val)
            head, head_reversed = head.next, head_reversed.next
        return maxval
        
        # #Use hashmap, time O(N), space O(N)
        # ptr = head
        # n = 0
        # htb = {}
        # while ptr:
        #     htb[n]= ptr.val
        #     n += 1
        #     ptr = ptr.next
        # ans = 0
        # for j in range(n//2):
        #     ans = max(ans, htb[j] + htb[n-1-j])
        # return ans
