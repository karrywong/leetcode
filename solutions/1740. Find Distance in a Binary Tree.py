# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        self.ans = -1
        def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
            if node is None:
                return -1, -1
            elif node.val == p and node.val == q:
                self.ans = 0
                return -1,-1
            
            left_val1, left_val2 = dfs(node.left) #-1,-1
            right_val1, right_val2 = dfs(node.right) #-1,2
                
            if left_val1 != -1 and right_val2 != -1 and self.ans == -1:
                self.ans = left_val1 + right_val2 + 2 
            
            if left_val2 != -1 and right_val1 != -1 and self.ans == -1:
                self.ans = left_val2 + right_val1 + 2 
                
            if left_val1 != -1: left_val1 += 1 # -1
            if left_val2 != -1: left_val2 += 1 # 1
            if right_val1 != -1: right_val1 += 1
            if right_val2 != -1: right_val2 += 1
                
            val1, val2 = -1,-1
            if node.val == p:
                val1 += 1 #0
                if left_val2 != -1 and self.ans == -1:
                    self.ans = left_val2
                if right_val2 != -1 and self.ans == -1:
                    self.ans = right_val2
                
            if node.val == q:
                val2 += 1 #0
                if left_val1 != -1 and self.ans == -1:
                    self.ans = left_val1
                if right_val1 != -1 and self.ans == -1:
                    self.ans = right_val1
                
            return max(val1, left_val1, right_val1), max(val2, left_val2, right_val2) 
        
        dfs(root)
        return self.ans
