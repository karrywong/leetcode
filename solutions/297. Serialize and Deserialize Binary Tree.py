# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque 
​
​
class Codec:
    #Leetcode soln - DFS, preorder transversal
    #Time: O(N), Space: O(N)
    def serialize(self, root:Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def preorder(node:Optional[TreeNode]) -> list[Optional[int]]:
            if node is None:
                return ['None']
            return [str(node.val)] + preorder(node.left) + preorder(node.right)
        return ",".join(preorder(root))
​
    def deserialize(self, data:str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def get_data(datas: list[str]) -> str:
            i = datas.popleft()
            yield i
            
        def helper() -> Optional[TreeNode]:
            val = next(get_data(dq))
            if val == 'None':
                return None
            node = TreeNode(int(val))
            node.left = helper()
            node.right = helper()
            return node
        dq = deque(data.split(','))
        return helper()
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
