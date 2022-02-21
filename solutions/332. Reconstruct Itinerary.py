class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #Almost identical but easier than 2097. Valid Arrangement of Pairs
        #Hierholzer's algorithm for Eulerian path
        graph = collections.defaultdict(list)        
        for s, e in tickets:
            graph[s].append(e)
                
        for k in graph:
            graph[k] = sorted(graph[k], reverse = True)
            
        ans = []
        ###stack implementation
        # stack = ['JFK']
        # while stack:
        #     while graph[stack[-1]]:
        #         stack.append(graph[stack[-1]].pop())
        #     ans.append(stack.pop())
        # return ans[::-1]
        
        ###DFS implementation
        def dfs(origin):
            while graph[origin]:
                dfs(graph[origin].pop())
            ans.append(origin)
        
        dfs('JFK')
        return ans[::-1]
