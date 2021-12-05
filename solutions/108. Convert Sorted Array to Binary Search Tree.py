# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        #Standard Tree problem 
        #Inorder traversal is not a unique identifier of BST
        #Time O(N), Space O(log(N)) due to height-balanced tree
        def helper(left, right):
            if left > right:
                return None
            
            p = left + (right - left) // 2 #right middle point, floor(n)
            # if (left + right) % 2: p += 1 //#left middle point, ceil(n)
            # if (left + right) % 2: p += randint(0,1)
            
            node = TreeNode(nums[p])
            node.left = helper(left, p-1)
            node.right = helper(p+1, right)
            return node
        return helper(0, len(nums)-1)
