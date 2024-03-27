# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        #soln 1 - Leetcode prefix sum + recursive preorder traversal, time O(N), space O(N)
        def preorder(node, cur_sum):
            if not node:
                return
            cur_sum += node.val
            #situation 1: prefix sum equal targetSum
            if cur_sum == targetSum: 
                self.count += 1
            #situation 2: subarray starting in middle equal targetSum
            #proof: cur_sum - (cur_sum - target) = target
            self.count += lib[cur_sum - targetSum]
            lib[cur_sum] += 1 #update
            
            #recursive preorder traversal
            preorder(node.left, cur_sum)
            preorder(node.right, cur_sum)
            
            #remove current sum from hashmap in order not to use it in parallel subtree
            lib[cur_sum] -= 1
            
        self.count = 0
        lib = collections.defaultdict(int)
        preorder(root, 0)
        return self.count
        
#         #soln 0 - Karry's recursion, time O(N^2), space O(N)
#         self.count = 0
#         def ListMake(lst, val):
#             temp = []
#             for i in lst:
#                 i += val
#                 if i == targetSum: self.count += 1
#                 temp.append(i)
#             return temp
        
#         def helper(node):
#             if not node:
#                 return []
#             if node.val == targetSum: self.count += 1
#             lst = [node.val]
#             if node.left:
#                 left_lst = helper(node.left)
#                 lst += ListMake(left_lst, node.val)
#             if node.right:
#                 right_lst = helper(node.right)
#                 lst += ListMake(right_lst, node.val)
#             # print(node.val, lst)
#             return lst
    
#         helper(root)
#         return self.count
