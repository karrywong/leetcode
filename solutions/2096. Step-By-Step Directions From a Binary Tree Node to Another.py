# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:        
    #eg1, 5->3, "XXXLL" -> "LL" -> "UU", 5->6, "XXXRL" -> "RL"
    #eg2, 2->2, "", 2->1, "L", "" + "L"
    #eg3, 1 startVal, 2 endVal, "L" -> "U", "U" + "" = "U"
    
    #Mock interview practice, time O(N), space O(N)
        def helper(node: Optional[TreeNode], target: int) -> str:
            if node is None:
                return ""
            if node.val == target:
                return "X"
​
            path = helper(node.left, target) #left child
            if len(path) > 0 :
                return "L"+path
​
            path = helper(node.right, target) #right child
            if len(path) > 0 :
                return "R"+path
            return ""
    
        startPath = helper(root, startValue)[:-1]
        destPath = helper(root, destValue)[:-1]
        i = 0 
        while i < len(startPath) and i < len(destPath) and startPath[i] == destPath[i]:
            i += 1
        return "U" * (len(startPath) - i) + destPath[i:]
