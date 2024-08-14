# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Codec:
​
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        def postorder(node: Optional[TreeNode]) -> list[str]:
            if node is None:
                return []
            return postorder(node.left) + postorder(node.right) + [str(node.val)]
        
        return " ".join(postorder(root))
​
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        def get_data(nums: list[int]) -> int: 
            i = nums.pop()
            yield i
            
        def helper(lower=float('-inf'), upper=float('inf')) -> Optional[TreeNode]:
            if not datas or datas[-1] < lower or datas[-1] > upper:
                return None
            val = next(get_data(datas))
            node = TreeNode(val)
            node.right = helper(val, upper)
            node.left = helper(lower, val)
            return node
            
        datas = [int(x) for x in data.split()]
        return helper()
        
​
# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
