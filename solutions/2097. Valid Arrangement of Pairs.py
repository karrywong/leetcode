class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        #Hierholzer's algorithm, inspired in discussion
        graph = collections.defaultdict(list)
        degree = collections.defaultdict(int)
        for s, e in pairs:
            graph[s].append(e)
            degree[s] += 1
            degree[e] -= 1
        
        start = pairs[0][0]
        for deg in degree:
            if degree[deg] == 1:
                start = deg
                break
        ans = []
        
        # ##Return Eulerian path via dfs.
        # def dfs(x): #recursion
        #     while graph[x]: 
        #         dfs(graph[x].pop())
        #     ans.append(x)
        # dfs(start)
​
        stack = [start] #iterative, idea from @delphih
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            ans.append(stack.pop())
        
        ans.reverse()
        return [[ans[i], ans[i+1]] for i in range(len(ans)-1)]
        
#         #First attempt, backtracking, time O(N!), TLE
#         pairs_set = set([tuple(pair) for pair in pairs])
#         self.ans = []
#         def dfs(choice, A):
#             if len(A) == len(pairs):
#                 self.ans = A[:]
#                 return
​
#             for tp in choice:
#                 if not A:
#                     A.append([tp[0],tp[1]])
#                     choice.remove(tp)
#                     dfs(choice, A)
#                     A.pop()
#                     choice.add(tp)
#                 else:
#                     if tp[0] == A[-1][1]:
#                         A.append([tp[0],tp[1]])
#                         choice.remove(tp)
#                         dfs(choice, A)
#                         A.pop()
#                         choice.add(tp)
#         dfs(pairs_set, [])
#         return self.ans
