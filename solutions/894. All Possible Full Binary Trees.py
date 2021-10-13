# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #soln 2 - memoization
    memo = {0:[], 1:[TreeNode(0)]}
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n%2 == 0:
            return []
        if n not in Solution.memo:
            ans = []
            for x in range(1,n): 
                y = n - 1 - x 
                for left in self.allPossibleFBT(x):
                    for right in self.allPossibleFBT(y):
                        bns = TreeNode(0)
                        bns.left = left
                        bns.right = right
                        ans.append(bns)
            Solution.memo[n] = ans
        return Solution.memo[n]
        
        #soln 1 - Jake's recursion idea
        #if n%2 == 0:
        #    return []
        #if n == 1:
        #    return [TreeNode(0)]
        #output = []
        #for i in range(1,n-1,2):
        #    leftTrees = self.allPossibleFBT(i)
        #    rightTrees = self.allPossibleFBT(n-i-1)
        #    for pairs in itertools.product(leftTrees,rightTrees):
