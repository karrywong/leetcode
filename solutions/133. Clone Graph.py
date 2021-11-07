"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
​
class Solution:
    def __init__(self):
        self.visited = {}
    def cloneGraph(self, node: 'Node') -> 'Node':
        # Soln 2 - Leetcode w BFS
        
        # # Soln 1 - Leetcode recursion w DFS
        if not node: 
            return node
        if node in self.visited:
            return self.visited[node]
        clone_node = Node(node.val, [])
        self.visited[node] = clone_node
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        return clone_node
    
        #Soln 0 - solution from Jake Reschke w BFS
#         if node:
#             nodeQ = collections.deque()
#             nodeQ.append(node)
#             copied = {node.val: Node(node.val)} # keys are node values, items are copied nodes
#             visited = set()                                     
#             while nodeQ:
#                 cur_node = nodeQ.popleft()
#                 visited.add(cur_node.val)
​
#                 for neighbor in cur_node.neighbors:
#                     if neighbor.val not in copied:  # make copy, establish connections
#                         new_node = Node(neighbor.val)
#                         copied[cur_node.val].neighbors.append(new_node) 
