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
#                 htb[node] = depth
#                 return depth
#             return htb[node]
#         dfs(root) #htb built
        
#         while root:
#             left_depth = htb[root.left] if root.left else 0
#             right_depth = htb[root.right] if root.right else 0
#             if left_depth == right_depth:
#                 return root
#             elif left_depth > right_depth:
#                 root = root.left
#             else: #left_depth < right_depth
#                 root = root.right
