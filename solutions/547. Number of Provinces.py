class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #first attempt, iterative dfs + stack
        n = len(isConnected)
        seen = set()
        ans = 0
        for i, row in enumerate(isConnected):
            if i in seen: continue
            for j in range(n):
                if j == i: continue
                if row[j] and j not in seen:
                    stack = [j]
                    seen.add(j)
                    while stack:
                        idx = stack.pop()
                        for k in range(n):
                            if k == j: continue
                            if isConnected[idx][k] and k not in seen:
                                stack.append(k)
                                seen.add(k)
                    ans += 1
        return ans + (n-len(seen))
                            
                
