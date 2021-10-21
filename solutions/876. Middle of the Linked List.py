# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # ### soln 2 - Leetcode soln, two pointers
        # slow = fast = head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        # return slow
               
        ###soln 1 - Leetcode soln, output to array, Time O(N), Space O(N)
        # arr = [head]
        # while arr[-1].next:
        #     arr.append(arr[-1].next)
        # return arr[arr//2]
      
        ##soln 0 - naive and trivial
        dummyhead = head
        count = 0
        while dummyhead:
            count += 1
            dummyhead = dummyhead.next
            
        count //= 2
        for i in range(count):
            head = head.next
        return head
        
