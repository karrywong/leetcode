"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
​
class Solution:    
    # def copyRandomList(self, head: 'Node') -> 'Node':
#         ## Soln 2 - my iterative w O(N) space, time O(N)
#         hash_map = {} #key: old node, value: new node
#         cur = head
#         ans = ListNode(None)
#         ans_ptr = ans
        
#         while cur:
#             ans_ptr.next = ListNode(cur.val)
#             hash_map[cur] = ans_ptr.next
#             cur = cur.next
#             ans_ptr = ans_ptr.next
        
#         cur = head
#         ans_ptr = ans.next
#         while cur:
#             ans_ptr.random = hash_map.get(cur.random)
#             cur = cur.next
#             ans_ptr = ans_ptr.next
#         return ans.next 
​
    def __init__(self):
            self.visitedHash = {}
    def copyRandomList(self, head: 'Node') -> 'Node':
       # Soln 1 - Leetcode recursive w DFS, time O(N), space O(N)
        if not head: return head
        if head in self.visitedHash:
            return self.visitedHash[head]
        node = ListNode(head.val)
        self.visitedHash[head] = node
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        return node
