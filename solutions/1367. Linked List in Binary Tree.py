# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        #Brute force, inspired by lee215
        #Time O(N*min(L,H)), Space O(H), w/ N = tree size, L = len(head), H = tree height
        def helper(linklst: ListNode, node: TreeNode) -> bool:
            if not linklst:
                return True
            if not node:
                return False
            return linklst.val == node.val and (helper(linklst.next, node.left) or helper(linklst.next, node.right))
        if not root:
            return False
        return helper(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
        
#         #Failed attempt - not include all checking possibilities
#         def helper(linklst: ListNode, node: TreeNode) -> bool:
#             if not linklst:
#                 return True
#             if not node:
#                 return False
#             if linklst.val == node.val:
#                 linklst = linklst.next
#             return helper(linklst, node.left) or helper(linklst, node.right)
#         return helper(head, root)
