# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
​
    def __init__(self, root: Optional[TreeNode]):
    #approach 1 - flatten tree into array, DOES NOT satisfy O(1) time and O(h) space requirement.
        # self.root = root
        # self.ptr = 0
        # self.lst = self.helper(self.root)
    # def helper(self, root):
    #     return self.helper(root.left) + [root.val] + self.helper(root.right) if root else []
    
        self.stack = []
        self._leftmost_inorder(root) #_:private
        
    def _leftmost_inorder(self, root):
        while root:
            self.stack.append(root)
            root = root.left
    
    def next(self) -> int:
        # val = self.lst[self.ptr]
        # self.ptr += 1
        # return val
        
        topmost_node = self.stack.pop()
        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)
        return topmost_node.val
​
    def hasNext(self) -> bool:
        # return True if self.ptr < len(self.lst) else False
        return len(self.stack) > 0
​
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
