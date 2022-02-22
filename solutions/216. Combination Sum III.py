class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        #First attempt, backtracking, time O( Permut(9,K) * K), space O(K) 
        # if sum(range(1, k+1)) > n:
        #     return []
        
        ans = []
        def backtrack(num=n, start=1, A=[]):
            if len(A) == k and num == 0:
                ans.append(A[:])
                return
            if len(A) > k or num < 0:
                return 
            for i in range(start, 10):
                A.append(i)
                backtrack(num-i, i+1, A)
                A.pop()
        backtrack()
        return ans
