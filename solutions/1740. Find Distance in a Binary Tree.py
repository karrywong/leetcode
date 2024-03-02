# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        # Two passes DFS
        def dfs(node: TreeNode, target: int) -> List[int]:
            if node is None:
                return []
            if node.val == target:
                return [node.val]
            
            left_lst = dfs(node.left, target)
            right_lst = dfs(node.right, target) 
            
            if len(left_lst) > 0:
                left_lst.append(node.val)
                return left_lst 
            if len(right_lst) > 0:
                right_lst.append(node.val)
                return right_lst
            return []
            
        p_lst = dfs(root, p) #[5,3]
        q_lst = dfs(root, q) #[7,2,5,3]
        
        ptr = -1
        prev = None
        while abs(ptr) < len(p_lst)+1 and abs(ptr) < len(q_lst)+1 and p_lst[ptr] == q_lst[ptr]:
            ptr -= 1
        return len(p_lst[:ptr+1]) + len(q_lst[:ptr+1])
        
        # Tediouss, one pass DFS
#         self.ans = -1
#         def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
#             if node is None:
#                 return -1, -1
#             elif node.val == p and node.val == q:
#                 self.ans = 0
#                 return -1,-1
            
#             left_val1, left_val2 = dfs(node.left) 
#             right_val1, right_val2 = dfs(node.right)
                
#             if left_val1 != -1 and right_val2 != -1 and self.ans == -1:
#                 self.ans = left_val1 + right_val2 + 2 
            
#             if left_val2 != -1 and right_val1 != -1 and self.ans == -1:
#                 self.ans = left_val2 + right_val1 + 2 
                
#             if left_val1 != -1: left_val1 += 1 
#             if left_val2 != -1: left_val2 += 1 
#             if right_val1 != -1: right_val1 += 1
#             if right_val2 != -1: right_val2 += 1
                
#             val1, val2 = -1,-1
#             if node.val == p:
#                 val1 += 1 #0
#                 if left_val2 != -1 and self.ans == -1:
#                     self.ans = left_val2
#                 if right_val2 != -1 and self.ans == -1:
#                     self.ans = right_val2
                
#             if node.val == q:
#                 val2 += 1 #0
#                 if left_val1 != -1 and self.ans == -1:
#                     self.ans = left_val1
#                 if right_val1 != -1 and self.ans == -1:
#                     self.ans = right_val1
                
#             return max(val1, left_val1, right_val1), max(val2, left_val2, right_val2) 
        
#         dfs(root)
#         return self.ans
