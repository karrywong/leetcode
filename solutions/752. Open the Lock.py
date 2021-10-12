from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
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
            if curPt == target:
                dist = 0
                while curPt != '0000':
                    curPt = pre[curPt]
                    dist += 1
                return dist
            neighbors = getNeighbors(curPt, deadends)
            
            for node in neighbors:
                if node not in visited:
                    ptQ.append(node)
                    visited[node] = None
                    pre[node] = curPt
        return -1
