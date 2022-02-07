class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #BFS approach     
        adjList = collections.defaultdict(set)
        for edge in edges:
            adjList[edge[0]].add(edge[1])
            adjList[edge[1]].add(edge[0])
            
        dq = collections.deque([source])
        seen = set()
        
        while dq:
            node = dq.popleft()
            if node == destination:
                return True
            for nextNode in adjList[node]:
                if nextNode not in seen:
                    seen.add(nextNode)
                    dq.append(nextNode)
        return False
                    
            
