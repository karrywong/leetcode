"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
​
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # #First attempt, recursion, straight forward, time O(N), space O(N)
        # if not root: return []
        # ans = []
        # for child in root.children:
        #     ans.extend(self.postorder(child))
        # ans.append(root.val)
        # return ans
        
        #Iterative, time O(N), space O(N)
        if not root: return []
        stack, ans = [root], []
        while stack:
            node = stack.pop()
            ans.append(node.val)
            stack.extend(node.children)
        return ans[::-1]
