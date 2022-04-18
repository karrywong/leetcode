# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ##Insightful follow-up question: What if the BST is modified (insert/delete operations) often   
        #and you need to find the kth smallest frequently? How would you optimize the kthSmallest   
        #routine?
        
        #2. Leetcode optimized, iterative inorder traversal plus stack
        #see similar (but in recursion) technique, 98. Validate Binary Search Tree
        #Tricky: Time O(H+k) due to stack append&pop, Space O(N)
        # stack = []
        # while True: 
        #     while root:
        #         stack.append(root)
        #         root = root.left
        #     root = stack.pop()
        #     k -= 1
        #     if not k:
        #         return root.val
        #     root = root.right
            
        #1. Brute-force, not optimized
        #Time O(N), Space O(N)
        # def helper(node):
        #     if not node: return []
        #     return helper(node.left) + [node.val] + helper(node.right)
        # return helper(root)[k-1]
        
        #Optimized recursion, still time O(N), space O(N)
        self.ans = -1
        self.count = k
        def inorder(node:Optional[TreeNode]) -> int:
            if not node:
                return
            inorder(node.left)
    
            self.count -= 1 #node itself        
            if self.count == 0: 
                self.ans = node.val
                return
​
            inorder(node.right)
            
        inorder(root)
        return self.ans
