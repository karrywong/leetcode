# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Codec:
    #Leetcode soln - DFS, preorder transversal
    #Time: O(N), Space: O(N)
    def serialize(self, root:Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # node.val + left, right
        # deque = [1, 2, None, None, 3, 4, None, None, 5, None, None]
        lst = []
        def dfs(node:Optional[TreeNode]) -> None:
            if node is None:
                lst.append('None')
                return
            
            lst.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            return
        
        dfs(root)
        print(" ".join(lst))
        return " ".join(lst)
​
    def get_data(self) -> str:
        for char in self.lst:
            yield char
        
    def deserialize(self, data:str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.lst = data.split()
        gen_data = self.get_data()
        def helper() -> TreeNode:
            char = next(gen_data)
            if char == 'None':
                return None
        
            node = TreeNode(int(char))
            node.left = helper()
            node.right = helper()
            return node
        
        return helper()
    
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
