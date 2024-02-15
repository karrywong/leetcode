class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        # n = 2, [2,1,2]
        # n = 3, [3,1,2,3,2], [2,3,2,1,3]
        # n = 4, [4, 2, 3, 2, 4, 3, 1]
        # n = 5, [5,3,1,4,3,5,2,4,2]
        
        # Gives a valid solution but not lexicographically largest
        ans = [1] * (2*n-1)
        def dfs(m:int=n) -> bool:
            if m == 1:
                return True
            for i in range(2*n-1-m):
                if ans[i] == 1 and ans[i+m] == 1:
                    ans[i], ans[i+m] = m, m
                    if dfs(m-1):
                        return True
                    ans[i], ans[i+m] = 1,1
            return False
        dfs()
        return ans    
        
#         # Time O(n!), space O(n)
#         m = 2*n - 1
#         ans = [0 for _ in range(m)] # 2n-1
#         seen = set()
#         def backtrack(idx:int = 0) -> bool:
#             if idx == m: #solution found
#                 return True
#             if ans[idx] != 0: #already filled, move on
#                 return backtrack(idx+1)
                
#             for v in range(n,0,-1):
#                 idy = idx if v==1 else v+idx
#                 if v not in seen and idy < m and ans[idy] == 0:
#                     ans[idx], ans[idy] = v, v
#                     seen.add(v)
#                     if backtrack(idx+1):
#                         return True
#                     ans[idx], ans[idy] = 0, 0
#                     seen.remove(v)
#             return False
                
#         backtrack() # assume answer aleady exists, ie backtrack() returns True
