#                 return result
            
#             else:
#                 if node in not_rob_saved:
#                     return not_rob_saved[node]
                
#                 rob = node.val + helper(node.left, True) + helper(node.right, True)
#                 not_rob = helper(node.left, False) + helper(node.right, False)
                
#                 result = max(rob, not_rob)
#                 not_rob_saved[node] = result
#                 return result
            
#         return helper(root, False)
        
        ### LeetCode solution - only recursion
        def helper(node):
            #return [rob this node, not rob this node]
            if not node: #at leaf
                return (0,0)
            
            left = helper(node.left)
            right = helper(node.right)
            
            #if we rob this node, we cannot rob its children
            rob = node.val + left[1] + right[1]
            
            #else we could choose to either rob its children or not
            not_rob = max(left) + max(right)
            
            # print(rob, not_rob)
            return [rob, not_rob]
        
        return max(helper(root))
