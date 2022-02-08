class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        #Recent attempt using BFS
        path = [[0]]
        dq = collections.deque(path)
        ans = []
        
        while dq:
            cur_path = dq.popleft()
            if cur_path[-1] == len(graph)-1:
                ans.append(cur_path[:])
                continue
            for node in graph[cur_path[-1]]:
                temp_path = cur_path[:]
                temp_path.append(node)
                dq.append(temp_path)
        return ans
        
#         #Leetcode top-down DP, time O(2^N*N), space O(2^N*N)
#         n = len(graph)
#         #recursion: allPathsToTarget(curNode) = curNode + allPathsToTarget(nextNode)
#         @lru_cache(maxsize=None)
#         def dp(cur): #compute all paths to target node
#             if cur == n-1:
#                 return [[cur]]
            
#             res = []
#             for ngh in graph[cur]:
#                 for path in dp(ngh): #compute all paths to the next node of the target node
#                     res.append([cur]+path)
#             return res
#         return dp(0)
​
        # #Second attempt, slightly different backtracking, time O(2^N*N), space O(2^N*N)
        # ans, n, A = [], len(graph), []
        # def dfs(val):
        #     A.append(val)
        #     if val == n-1: ans.append(A[:])
        #     for val_next in graph[val]:
        #         dfs(val_next)
        #     A.pop()
        # dfs(0)
        # return ans
    
        # #First attempt, backtracking, time O(2^N*N), space O(2^N*N)
        # ans, n = [], len(graph)
        # def backtrack(val, A=[]):
        #     if val == n-1: 
        #         ans.append(A[:])            
        #     for ngh in graph[val]:
        #         A.append(ngh)
        #         backtrack(ngh, A)
        #         A.pop()
        # backtrack(0,[0])
        # return ans
