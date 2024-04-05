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
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def preorder(node, string) -> str: #preorder traversal
            if not node:
                string += 'None,'
            else:
                string += str(node.val) + ','
                string = preorder(node.left, string)
                string = preorder(node.right, string)
            return string
        return preorder(root, '')
​
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def btFromPreorder(dq) -> Optional[TreeNode]:
            if dq[0] == 'None':
                dq.popleft()
                return None
            
            root = TreeNode(dq[0])
            dq.popleft()
            root.left = btFromPreorder(dq)
            root.right = btFromPreorder(dq)
            return root
            
        data_queue = deque(data.split(','))
        return btFromPreorder(data_queue)
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
