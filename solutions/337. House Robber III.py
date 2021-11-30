        dp_rob = [0] * (index+1)
        # represent the maximum start by node i without robbing i
        dp_not_rob = [0] * (index+1)        
        
        for i in range(index, -1, -1):
            if i not in graph: #node i is a leaf
                dp_rob[i] = tree[i]
                dp_not_rob[i] = 0
            else:
                dp_rob[i] = tree[i] + sum(dp_not_rob[j] for j in graph[i])
                dp_not_rob[i] = sum(max(dp_rob[j], dp_not_rob[j]) for j in graph[i])
        
        return max(dp_rob[0], dp_not_rob[0])
    
#         #soln 1 - Leetcode recursion w memoization
#         rob_memo, not_rob_memo = {}, {}
        
#         def helper(node, parent_robbed = False):
#             if not node: 
#                 return 0
            
#             if parent_robbed:
#                 #cannot rob this node
#                 if node in rob_memo:
#                     return rob_memo[node]
#                 val = helper(node.left, False) + helper(node.right, False)
#                 rob_memo[node] = val
#                 return val
#             else:
#                 #calculate 'rob' and 'not rob', return max(rob, not_rob)
#                 if node in not_rob_memo:
#                     return not_rob_memo[node]
#                 rob = node.val + helper(node.left, True) + helper(node.right, True)
#                 not_rob = helper(node.left, False) + helper(node.right, False)
#                 val = max(rob, not_rob)
#                 not_rob_memo[node] = val
#                 return val
#         return helper(root)
        
#         #soln 0 - Leetcode recursion, time complexity O(N), space O(1)
#         def helper(node): #return (rob, not_rob)
#             if not node:
#                 return (0,0)
            
#             left = helper(node.left)
#             right = helper(node.right)
            
#             #if we rob this node, we cannot rob its children
#             rob = node.val + left[1] + right[1]
#             #else we could choose to either rob its children or not
#             not_rob = max(left) + max(right)
            
#             return (rob, not_rob)
#         return max(helper(root))
