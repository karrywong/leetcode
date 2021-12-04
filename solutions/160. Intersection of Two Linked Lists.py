# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        #LeetCode two pointers, really clever, time: O(M+N), space O(1)
        #diagram in mind a+c+b = b+c+a, where b>a and c is the length of the intersection part
        Aptr, Bptr = headA, headB
        while Aptr != Bptr:
            Aptr = headB if Aptr is None else Aptr.next
            Bptr = headA if Bptr is None else Bptr.next
        return Aptr
        
        # #First attempt, hashtable, time O(M+N), space O(M), M: len(headA), N: len(headB)
        # libA = set()
        # Aptr = headA
        # while Aptr:
        #     libA.add(Aptr)
        #     Aptr = Aptr.next
        # Bptr = headB
        # while Bptr:
        #     if Bptr in libA:
        #         return Bptr
        #     Bptr = Bptr.next
        # return None
