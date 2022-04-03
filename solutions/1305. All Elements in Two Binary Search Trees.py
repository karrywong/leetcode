# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        #Time O(N), space O(N), straightforward by flattening two BSTs
        def helper(node):
            if not node:
                return []
            return helper(node.left) + [node.val] + helper(node.right)
        
        lst1 = helper(root1)
        lst2 = helper(root2)
        i, j = 0, 0
        ans = []
        while i < len(lst1) and j < len(lst2):
            if lst1[i] <= lst2[j]:
                ans.append(lst1[i])
                i += 1
            else:
                ans.append(lst2[j])
                j += 1
        if i == len(lst1):
            ans.extend(lst2[j:])
        else: #j == len(lst2)
            ans.extend(lst1[i:])
        return ans
