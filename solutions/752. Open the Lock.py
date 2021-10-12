from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        #soln 2 - Leetcode's solution
        def neighbors(node):
            for i in range(0,4):
                x = int(node[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    yield node[:i] + str(y) + node[i+1:]
        dead = set(deadends)
        queue = collections.deque([('0000', 0)])
        seen = {'0000'}
        while queue:
            node, depth = queue.popleft()
            if node == target: return depth
            if node in dead: continue
            for nei in neighbors(node):
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth+1))
        return -1
        
        #soln 1 - Jake's BFS
        def getNeighbors(s, deadends):
            neighbors = []
            for i in range(0,4):
                temp = s[0:i] + str((int(s[i])+1)%10) + s[i+1:]
                if temp not in deadends:
                    neighbors.append(temp)
                temp = s[0:i] + str((int(s[i])-1)%10) + s[i+1:]
                if temp not in deadends:
                    neighbors.append(temp)
            return neighbors
​
        ptQ = deque()
        visited = {}
        visited['0000'] = None
        deadends = set(deadends)
        if '0000' not in deadends:
            ptQ.append('0000')
        pre = {}        
        while ptQ:
            curPt = ptQ.popleft()
            # Any additional code
