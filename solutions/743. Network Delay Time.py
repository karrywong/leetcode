class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra algorithm, time O(ElogV) = O(NlogN), space O(N)
        graph = collections.defaultdict(set)
        for u, v, w in times:
            graph[u].add((v,w))
            
        hp = [(0,k)]
        heapq.heapify(hp)
        visited = {}
        
        while hp:
            time, node = heapq.heappop(hp)
            if node not in visited:
                visited[node] = time
                for ngh, ngh_time in graph[node]:
                    if ngh not in visited:
                        heapq.heappush(hp, (time+ngh_time, ngh))
                        
        return max(visited.values()) if len(visited) == n else -1
