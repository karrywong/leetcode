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
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def _get_list(node:Optional[ListNode]) -> List[int]:
            res = []
            while node:
                res.append(node.val)
                node = node.next
            return res
        
        vals = _get_list(head)
        
        def _convert_lst_to_BST(l:int, r:int) -> Optional[TreeNode]:
            if l > r:
                return None
            
            mid = l + (r-l)//2
            node = TreeNode(vals[mid])
            
            if l == r:
                return node
            node.left = _convert_lst_to_BST(l, mid-1)
            node.right = _convert_lst_to_BST(mid+1, r)
            return node
        
        return _convert_lst_to_BST(0,len(vals)-1)
