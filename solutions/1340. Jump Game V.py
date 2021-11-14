class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n, lib = len(arr), collections.defaultdict(list)
        for i, v in enumerate(arr):
            lib[v].append(i)
        lib = dict(sorted(lib.items()))
        dp = [1] * n
        
        for val in lib:
            for i in lib[val]:
                for j in range(i+1, min(i+d+1, n)):
                    if arr[j] < val:
                        dp[i] = max(dp[i], 1+dp[j])
                    else: 
                        break
                for j in range(i-1, max(i-d-1, -1),-1):
                    if arr[j] < val:
                        dp[i] = max(dp[i], 1+dp[j])
                    else: 
                        break
        return max(dp)
