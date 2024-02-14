class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        # n = 2, [2,1,2]
        # n = 3, [3,1,2,3,2], [2,3,2,1,3]
        # n = 4, [4, 2, 3, 2, 4, 3, 1]
        
        # Time O(n!), space O(n)
        m = 2*n - 1
        ans = [0 for _ in range(m)] # 2n-1
        seen = set()
        def backtrack(idx:int = 0) -> bool:
            if idx == m: #solution found
                return True
            if ans[idx] != 0: #already filled, move on
                return backtrack(idx+1)
                
            for v in range(n,0,-1):
                idy = idx if v==1 else v+idx
                if v not in seen and idy < m and ans[idy] == 0:
                    ans[idx], ans[idy] = v, v
                    seen.add(v)
                    if backtrack(idx+1):
                        return True
                    ans[idx], ans[idy] = 0, 0
                    seen.remove(v)
            return False
                
        backtrack() # assume answer aleady exists, ie backtrack() returns True
        return ans 
            
#         # O(n!)  
#         # Failed attempt
#         ans = [0 for _ in range(2*n)] # 2n
#         def helper(i:int, ans: List[int]) -> None:
#             if i == 1:
#                 for idx, x in enumerate(ans):
#                     if x == 0:
#                         ans[idx] = 1
#                 return
            
#             for idx in range(n):
#                 if ans[idx] == 0 and ans[idx+i] == 0:
#                     ans[idx], ans[idx+i] = i, i
#                     break
