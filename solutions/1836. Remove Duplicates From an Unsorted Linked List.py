# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        #First attempt, first sweep to record duplicates 
        htb = collections.defaultdict(int)
        ptr = head
        while ptr:
            htb[ptr.val] += 1
            ptr = ptr.next
            
        to_be_delete = set([k for k, v in htb.items() if v > 1])
        if not to_be_delete:
            return head
        sentinel = ListNode(0, head)
        prev = sentinel
        cur = head
        while cur: 
            if cur.val in to_be_delete:
                while cur and cur.val in to_be_delete:
                    cur = cur.next
                prev.next = cur
            prev = prev.next
            if not cur:
                break
            cur = cur.next
        return sentinel.next
