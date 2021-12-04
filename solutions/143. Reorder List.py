# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #Too many failed attempts, Leetcode solution - subproblems:
        #First, find middle node, 876. Middle of the Linked List
        #Second, reverse the 2nd part, 206. Reverse Linked List
        #Third, merge two Lists, 21. Merge Two Sorted Lists
​
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev, cur = None, slow
        while cur:
            next_temp = cur.next
            cur.next = prev
            prev = cur
            cur = next_temp    
            #cur.next, prev, cur = prev, cur, cur.next //more elegant
        
        first, second = head, prev
        while second.next:
            temp = first.next
            first.next = second
            first = temp
            #first.next, first = second, first.next
            
            temp = second.next
            second.next = first
            second = temp
            #second.next, second = first, second.next
