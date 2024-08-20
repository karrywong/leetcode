# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        # two-pass, time O(N), space O(N)
        lookup = {None:-1}
        def helper(node, parent=None):
            lookup[node] = lookup.get(parent) + 1
            if node.left: 
                helper(node.left, node)
            if node.right:
                helper(node.right, node)
            return
        helper(root)
        depth = max(lookup.values())
        
        def get_ans(node) -> TreeNode:
            if not node:
                return None
            if lookup[node] == depth:
                return node
            
            left_ans = get_ans(node.left)
            right_ans = get_ans(node.right)
            return node if left_ans and right_ans else left_ans or right_ans
        
        return get_ans(root)
        
        # #Leetcode recursion, time O(N), space O(N)
        # def dfs(node) -> Tuple[Optional[TreeNode], int]:
        #     if node is None:
        #         return None, 0
        #     left_node, left_dist = dfs(node.left)
        #     right_node, right_dist = dfs(node.right)
        #     if left_dist > right_dist: 
        #         return left_node, left_dist+1
        #     elif left_dist < right_dist:
        #         return right_node, right_dist+1
        #     else:
        #         return node, left_dist+1
        # ans, _ = dfs(root)
        # # print(depth)
        # return ans
        
#         #Karry's first attempt with Jake's help, DFS with memoization on depth, two passes
#         htb = {} #key = node, value = depth
#         def dfs(node):
#             if not node:
#                 return 0
#             if node not in htb:
#                 left = dfs(node.left)
#                 right = dfs(node.right)
#                 depth = max(left, right) + 1
