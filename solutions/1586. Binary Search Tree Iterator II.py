# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    #More challenging than problem, 173. Binary Search Tree Iterator
    def __init__(self, root: Optional[TreeNode]):
        # # approach 1 - flatten tree into array, DOES NOT follow-up.
        # self.root = root
        # self.ptr = -1
        # self.lst = self.helper(self.root)
    # def helper(self, root):
    #     return self.helper(root.left) + [root.val] + self.helper(root.right) if root else []
​
        #LeetCode iterative inorder traversal, time O(1) (amortized if needed) for all calls, O(N) space
        self.last = root
        self.stack, self.arr = [], []
        self.pointer = -1
        
    def hasNext(self) -> bool:
        # return self.ptr < len(self.lst)-1
        return self.stack or self.last or self.pointer < len(self.arr)-1
        
    def next(self) -> int:
        # self.ptr += 1
        # return self.lst[self.ptr]   
        
        self.pointer += 1
        if self.pointer == len(self.arr):
            while self.last:
                self.stack.append(self.last)
                self.last = self.last.left
            curr = self.stack.pop()
            self.last = curr.right
            
            self.arr.append(curr.val)
        return self.arr[self.pointer]
        
    def hasPrev(self) -> bool:
        # return self.ptr > 0
        return self.pointer > 0 
    
    def prev(self) -> int:
        # self.ptr -= 1
        # return self.lst[self.ptr]   
        
        self.pointer -= 1
        return self.arr[self.pointer]
​
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.hasNext()
# param_2 = obj.next()
# param_3 = obj.hasPrev()
# param_4 = obj.prev()
