"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""
​
class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        #Almost identical but slightly trickier than 543. Diameter of Binary Tree 
        # soln 0 - DFS, time O(N), space O(N)
        self.diameter = 0 
        def helper(node):            
            # lst_path = []
            # heapq.heapify(lst_path)
            max_val = float('-inf')
            sec_max_val = float('-inf')
            for ch in node.children:
                val = helper(ch)
                if max_val == float('-inf'):
                    max_val = val
                elif val > max_val:
                    sec_max_val = max_val
                    max_val = val
                elif val > sec_max_val:
                    sec_max_val = val
                
            if max_val == float('-inf'):
                return 1
            
            if sec_max_val > float('-inf'):
                self.diameter = max(self.diameter, max_val + sec_max_val)
                return max(max_val, sec_max_val) + 1
            else: 
                self.diameter = max(self.diameter,max_val)
                return max_val+1
            
        helper(root)
        return self.diameter
