# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        #LeetCode Sentinel, time O(N), space O(1)
        #sentinel head
        sentinel = ListNode(0)
        sentinel.next = head
        not_nine = sentinel
        
        while head: #find rightmost non-nine digit
            if head.val != 9:
                not_nine = head
            head = head.next
            
        not_nine.val += 1
        not_nine = not_nine.next
        while not_nine:
            not_nine.val = 0
            not_nine = not_nine.next
        return sentinel if sentinel.val else sentinel.next
        
#         #First attempt, time O(N+N) = O(N), space O(N) 
#         lst = []
#         while head:
#             lst.append(head)
#             head = head.next
​
#         ans = lst.pop()
#         if ans.val == 9:
#             ans.val = 0
#             carry = 1
#         else:
#             ans.val += 1
#             carry = 0
            
#         while lst:
#             node = lst.pop()
#             if carry and node.val == 9:
#                 node.val = 0
#                 carry = 1
#             elif carry:
#                 node.val += 1
#                 carry = 0
#             node.next = ans
#             ans = node
            
#         if carry:
#             node = ListNode(1)
#             node.next = ans
#             ans = node
#         return ans
