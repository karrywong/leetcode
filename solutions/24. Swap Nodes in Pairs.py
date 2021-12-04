# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #second attempt, iterative, Time O(N), Space O(1)
        head_ptr1 = ListNode(-1)
        head_ptr1.next = head  
        prev_node = head_ptr1 #preNode (dummy) stores pointer to the head node
        
        while head and head.next:
            #nodes to be swapped
            first = head
            second = head.next
            
            #swapping
            prev_node.next = second #-1 -> 2->
            first.next = second.next # 1-> 3
            second.next = first # 2 -> 1
            
            #Reinitialize head and prev_node for next swap
            prev_node = first 
            head = first.next
            
        return head_ptr1.next
    
#         #first attempt w/ Jake, recursion, Time O(N), Space O(N)
#         if not head: return head #empty 
#         if not head.next: return head #one node
        
#         head_ptr1 = head
#         head_ptr2 = head.next
        
#         head_ptr1.next = self.swapPairs(head.next.next) #1->3
#         head_ptr2.next = head_ptr1 #2->1
​
#         return head_ptr2 #2->
