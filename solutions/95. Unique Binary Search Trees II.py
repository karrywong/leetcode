# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        #LeetCode recursion - idea from problem 96. Unique Binary Search Trees
        memo = {}
        def generate_trees(start, end):
            if start > end:
                return [None]
            if (start, end) in memo:
                return memo[(start, end)]
            
            ans = [] #all possible trees
            for i in range(start, end+1):
                lbst = generate_trees(start, i-1)
                rbst = generate_trees(i+1, end)
​
                for l in lbst:
                    for r in rbst:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        ans.append(root)
            memo[(start, end)] = ans
            return ans
        
        return generate_trees(1, n)
