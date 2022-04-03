"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
​
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # #First attempt, recursion, straight forward, time O(N), space O(N)
        # if not root: return []
        # ans = [root.val]
        # for child in root.children:
        #     ans.extend(self.preorder(child))
        # return ans
    
        #Iterative, time O(N), space O(N)
        if not root: return []
        stack, ans = [root], []
        while stack:
            node = stack.pop()
            ans.append(node.val)
            stack.extend(node.children[::-1])
        return ans
        
