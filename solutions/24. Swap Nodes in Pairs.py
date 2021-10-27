# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #first attempt, Time O(N), Space O(N)
        if not head: return head #empty 
        if not head.next: return head #one node
        
        head_ptr1 = head
        head_ptr2 = head.next
        
        head_ptr1.next = self.swapPairs(head.next.next) #1->3
        head_ptr2.next = head_ptr1 #2->1
​
        return head_ptr2
