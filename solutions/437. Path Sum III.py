# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        #soln 0 - Karry's recursion 
        self.count = 0
        def ListMake(lst, val):
            temp = []
            for i in lst:
                i += val
                if i == targetSum: self.count += 1
                temp.append(i)
            return temp
        
        def helper(node):
            if not node:
                return []
            if node.val == targetSum: self.count += 1
            lst = [node.val]
            if node.left:
                left_lst = helper(node.left)
                lst += ListMake(left_lst, node.val)
            if node.right:
                right_lst = helper(node.right)
                lst += ListMake(right_lst, node.val)
            return lst
    
        helper(root)
        return self.count
