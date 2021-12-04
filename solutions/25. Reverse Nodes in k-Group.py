# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #LeetCode recursion, time O(N), space O(N/k) due to recursion stack
        def reverseLinkList(head, k):
            rev_head, ptr = None, head
            while k:
                next_node = ptr.next #keep track of next node
                #insert node "ptr" at the beginning of reversed linked list
                ptr.next = rev_head 
                rev_head = ptr
                ptr = next_node #move on to next node
                k -=1
            return rev_head
        
        count = 0
        ptr = head
        
        while count < k and ptr:
            ptr = ptr.next
            count += 1
        
        if count == k:
            reversedHead = reverseLinkList(head, k)
            head.next = self.reverseKGroup(ptr, k)
            return reversedHead
        return head
    
        # # second attempt by Jake
        # if k == 1: return head
        # scan = head
        # new_head = None
        # old_tail = None
        # stack = []
        # while True:
        #     if len(stack) < k:
        #         stack.append(scan)
        #     else:
        #         last = stack.pop()
        #         last.next = stack[-1]
        #         if not new_head:
        #             new_head = last
        #         else:
        #             old_tail.next = last
        #         for _ in range(k - 2):
        #             last = stack.pop()
        #             last.next = stack[-1]
        #         last = stack.pop()
        #         last.next = scan
        #         old_tail = last
        #         stack.append(scan)
        #     if scan:
        #         scan = scan.next
        #     else:
        #         return new_head
