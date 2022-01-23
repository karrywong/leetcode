# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #Overcomplicatede, simple Leetcode soln, first form a cycle and then break it
        #Time O(N), space O(1)
        if not head: 
            return head
        if not head.next:
            return head
        
        n = 1
        ptr = head
        while ptr.next:
            ptr = ptr.next
            n += 1
        ptr.next = head
        
        new_ptr = head
        if k >= n: k %= n
        count = n-k-1
        
        while count:
            new_ptr = new_ptr.next
            count -= 1
            
        new_head = new_ptr.next
        new_ptr.next = None
        return new_head
