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
    def copyRandomList(self, head: 'Node') -> 'Node':
        lookup = {} #key: old node, value: new node
        ans = Node(0) #sentinel
        ans_ptr = ans
        cur = head
        
        while cur:
            ans_ptr.next = Node(cur.val)
            lookup[cur] = ans_ptr.next
            cur = cur.next
            ans_ptr = ans_ptr.next
        
        cur = head
        ans_ptr = ans.next
        while ans_ptr:
            ans_ptr.random = lookup.get(cur.random)
            cur = cur.next
            ans_ptr = ans_ptr.next
            
        return ans.next
​
    # def __init__(self):
    #         self.visitedHash = {}
    
    # def copyRandomList(self, head: 'Node') -> 'Node':
#         ## Soln 2 - Leetcode iterative w O(N) space
#         def getClonedNode(node):
#             if node:
#                 if node in self.visitedHash:
#                     return self.visitedHash[node]
#                 else:
#                     self.visitedHash[node] = Node(node.val, None, None)
#                     return self.visitedHash[node]
#             return None
        
#         if not head: return head
#         old_node = head
#         new_node = Node(old_node.val, None, None)
#         self.visitedHash[old_node] = new_node
        
#         while old_node:
#             new_node.random = getClonedNode(old_node.random)
#             new_node.next = getClonedNode(old_node.next)
#             old_node = old_node.next
#             new_node = new_node.next
            
#         return self.visitedHash[head]
    
        # # Soln 1 - Leetcode recursive w DFS
        # if not head: return head
        # if head in self.visitedHash:
        #     return self.visitedHash[head]
        # node = Node(head.val, None, None)
        # self.visitedHash[head] = node
        # node.next = self.copyRandomList(head.next)
        # node.random = self.copyRandomList(head.random)
        # return node
