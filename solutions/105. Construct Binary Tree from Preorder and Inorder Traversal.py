# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #Useful to refer to similar but easier problem, 108. Convert Sorted Array to Binary Search Tree
        #Totally stuck w too many failed attempts, leetcode solution - recursion
        #Time O(N), Space O(N) due to hash map, worst case in space: skew tree
        def helper(left, right):
            if left > right:
                return None
            node_val = preorder[self.preorder_index]
            node = TreeNode(node_val)
            self.preorder_index += 1
            
            node.left = helper(left, inorder_htb[node_val]-1)
            node.right = helper(inorder_htb[node_val]+1, right)
            return node
            
        self.preorder_index = 0
        #{value: index} for inorder
        inorder_htb = {v : k for k, v in enumerate(inorder)}
        
        return helper(0, len(preorder)-1)
