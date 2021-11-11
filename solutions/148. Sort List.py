# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #soln 1 - Leetcode top-down merge sort
        def getMid(head):
            slow = fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            dummyhead = head
            while slow.next:
                slow = slow.next
                dummyhead = dummyhead.next
            mid = dummyhead.next
            dummyhead.next = None
            return mid
        
        def merge(list1, list2):
            dummyhead = ListNode();
            tail = dummyhead
            while list1 and list2:
                if (list1.val < list2.val):
                    tail.next = list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    list2 = list2.next
                tail = tail.next
            tail.next = list1 if list1 else list2
            return dummyhead.next
​
        if not head or not head.next:
            return head
        mid = getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return merge(left, right)
​
        # #soln 0 - naive attempt, two pass, Space O(N)
        # if not head: return head
        # stack = []
        # while head:
        #     stack.append(head.val)
        #     head = head.next
        # stack.sort(reverse=True)
        # ans_ptr = ListNode(stack.pop())
        # ans = ans_ptr
        # while stack:
        #     ans_ptr.next = ListNode(stack.pop())
        #     ans_ptr = ans_ptr.next
        # return ans
