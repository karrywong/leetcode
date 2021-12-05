class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        #Leetcode's two array, don't rush into graph related structures like adjacency list, etc.
        #time O(E), space O(N)
        if len(trust) < n-1: return -1 #corner case
        # indegree = [0]*n
        # outdegree = [0]*n
        degree = [0]*n
        
        for t in trust:
            # indegree[t[1]-1] += 1
            # outdegree[t[0]-1] +=1
            degree[t[1]-1] += 1
            degree[t[0]-1] -= 1
        
        for i in range(n):
            # if indegree[i] == n-1 and outdegree[i] == 0:
            if degree[i] == n-1:
                return i+1
        return -1
        
        #Failed attempt, wrong concept!!!
        # guess = set()
        # trust.sort()
        # print(trust)
        # #corner case, if trust = [] and n=1, judge is 1 else -1
        # if not trust: return n if n==1 else -1 
        # for i in range(len(trust)):
        #     a, b = trust[i]
        #     print(a,b,guess)
        #     if a in guess:
        #         guess.remove(a)
        #         continue
        #     if b not in guess:
        #         guess.add(b)
        # return list(guess)[0] if len(guess) == 1 else -1
