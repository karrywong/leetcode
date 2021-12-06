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
        def preorder(node, string): #preorder traversal
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
        def btFromPreorder(lst):
            if lst[0] == 'None':
                lst.pop(0)
                return None
            
            root = TreeNode(lst[0])
            lst.pop(0)
            root.left = btFromPreorder(lst)
            root.right = btFromPreorder(lst)
            return root
            
        data_list = data.split(',')
        return btFromPreorder(data_list)
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
