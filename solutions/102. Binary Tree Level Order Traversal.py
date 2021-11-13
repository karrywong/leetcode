# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #soln 1 - recursion
        ans = []
        if not root:
            return root
        
        def helper(node, level):
            if len(ans) == level:
                ans.append([])
            ans[level].append(node.val)
            
            if node.left:
                helper(node.left, level+1)
            if node.right:
                helper(node.right, level+1)
        helper(root, 0)
        return ans
    
        # #soln 0 - first attempt w deque
        # if not root: return root
        # ans = []
        # queue = collections.deque([root])
        # while queue:
        #     size = len(queue)
        #     temp = []
        #     for i in range(size):
        #         node = queue.popleft()
        #         temp.append(node.val)
        #         if node.left: queue.append(node.left)
        #         if node.right: queue.append(node.right)
        #     ans.append(temp)
        # return ans
