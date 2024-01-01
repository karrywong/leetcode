from collections import Counter
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        # brute O(2^n * n^2)
        # [2,4,6] -> {2:1, 4:1, 6:1}, k=2
        # ans = 3 
        
        # O(NlogN + N + N^2) ~ O(N^2)
        # [1,2,4,7,11], k = 5
        # [1,2,4,7,11] -> [1,2,3,4]
        # ans = 5 + 4 +2 +2 + 1
        # 
        # ans = 5 + 4 (x=1, 1, 1+2, 1+2+3, 1+2+3+4) 
    
    # solution by lee215 (see solution)
    # time O(nlogn + k), space O(n + k)
    # dp0 is the ways that without A[i]
    # dp1 is the ways that with A[i]
        count = [Counter() for i in range(k)]
        for a in nums:
            count[a % k][a] += 1
            
        res = 1
        for i in range(k):
            prev, dp0, dp1 = 0, 1, 0
            for a in sorted(count[i]):
                v = pow(2, count[i][a])
                if prev + k == a:
                    dp0, dp1 = dp0+dp1, dp0 * (v-1)
                else:
                    dp0, dp1 = dp0+dp1, (dp0+dp1) * (v-1)
                prev = a
