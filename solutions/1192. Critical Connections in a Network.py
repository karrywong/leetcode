class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        #Tarjan's bridge-finding algorithm, linear time O(V+E), space O(V)<https://en.wikipedia.org/wiki/Bridge_%28graph_theory%29#Tarjan's_bridge-finding_algorithm>
        #Refer to Problem 22-2 in CLRS
        
        #Soln 1 - Inspired by jo-va's soln, refer to YouTube video <https://youtu.be/aZXi1unBdJA>
        graph = collections.defaultdict(set)
        for u, v in connections:
            graph[u].add(v)
            graph[v].add(u)
        
        depth = [None] * n
        low_link = [None] * n
        visited = [False] * n
        bridges = []
                
        def find_bridges():
            cur_depth = -1
            for i in range(n):
                if not visited[i]:
                    dfs(-1,i,cur_depth)
            
        def dfs(parent, node,cur_depth):
            visited[node] = True
            cur_depth += 1
            low_link[node] = cur_depth
            depth[node] = cur_depth
            for next_node in graph[node]:
                if next_node == parent:
                    continue
                if not visited[next_node]:
                    dfs(node, next_node, cur_depth)
                    low_link[node] = min(low_link[node], low_link[next_node])
                    if depth[node] < low_link[next_node]:
                        bridges.append([node, next_node])
                else:
                    low_link[node] = min(low_link[node], depth[next_node])
        
        find_bridges()
        return bridges
