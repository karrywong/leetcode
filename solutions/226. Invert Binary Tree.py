# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #soln 2 - BFS
        if not root: 
            return root
        queue = collections.deque()
        queue.append(root)
        while queue:
            cur_node = queue.popleft()
            cur_node.left, cur_node.right = cur_node.right, cur_node.left
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
        return root
    
        #soln 1 - recursion
        #base case 
        #if not root:
        #    return root
        #else: # leave the root alone
            # then apply invertTree to left and right subtree
            # swap left tree and right tree
            #print(root.right, root.left)
        #    root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        #    return root
