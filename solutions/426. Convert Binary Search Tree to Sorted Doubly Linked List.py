"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
​
class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def helper(node: 'Optional[Node]') -> Tuple['Optional[Node]', 'Optional[Node]']:
            if node is None:
                return None, None
            
            left_head, left_tail = helper(node.left)
            right_head, right_tail = helper(node.right)
            
            if left_head:
                node.left = left_tail
                left_tail.right = node
            else:
                left_head = node
                
            if right_tail:
                node.right = right_head
                right_head.left = node
            else:
                right_tail = node
            
            return left_head, right_tail
        
        if root is None: return root
        head, tail = helper(root)
        head.left = tail
        tail.right = head
        
        return head
