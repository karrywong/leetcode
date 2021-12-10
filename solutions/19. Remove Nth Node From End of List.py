# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Time: O(N), Space O(1)
        slow = fast = head
        count = 0
        while fast and count < n:
            fast = fast.next
            count += 1
        
        ans = ListNode(0, head)
        ans_ptr = ans 
        while fast:
            ans_ptr = ans_ptr.next
            fast = fast.next
            slow = slow.next
        
        ans_ptr.next = slow.next
        return ans.next
