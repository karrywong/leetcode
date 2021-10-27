# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #soln 0 - first attempt
        if not head or not head.next: 
            return False
        else:
            lib = {}
            
        head_ptr = head
        prev = head
        head_ptr = head_ptr.next
        while head_ptr:
            if head_ptr in lib: 
                if lib[head_ptr] == prev:
                    return True
            else:
                lib[head_ptr] = prev
            head_ptr = head_ptr.next
        return False
        
