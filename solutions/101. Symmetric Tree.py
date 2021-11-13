# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # soln 1 - LeetCode recursion
        # def isMirror(t1, t2):
        #     if not t1 and not t2:
        #         return True
        #     if not t1 or not t2:
        #         return False
        #     return (t1.val == t2.val) and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
        # return isMirror(root, root)
        
        #soln 2 - LeetCode iterative
        queue = collections.deque([root, root])
        while queue:
            t1 = queue.pop()
            t2 = queue.pop()
            if t1 is None and t2 is None: continue
            if t1 is None or t2 is None: return False
            if t1.val != t2.val: return False
            queue.append(t1.left)
            queue.append(t2.right)
            queue.append(t1.right)
            queue.append(t2.left)
        return True
