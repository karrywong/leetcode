# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        #Inorder Traversal w O(1) space by bindloss
        self.prev, self.res = None, []
        self.max_count, self.cur_count = 0, 
        
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.cur_count = 1 if node.val != self.prev else self.cur_count + 1
            if self.cur_count == self.max_count:
                self.res.append(node.val)
            if self.cur_count > self.max_count:
                self.res = [node.val]
                self.max_count = self.cur_count
            self.prev = node.val
            dfs(node.right)    
        dfs(root)
        return self.res    
        
        # #First attempt, Time Complexity O(N), Space Complexity O(N)
        # self.counter = collections.defaultdict(int)
        # def helper(node):
        #     if node:
        #         self.counter[node.val] += 1
        #         helper(node.left)
        #         helper(node.right)
        # helper(root)
        # maxval = max(self.counter.values())
        # ans = []
        # for k in self.counter:
        #     if self.counter[k] == maxval:
        #         ans.append(k)
        # return ans
