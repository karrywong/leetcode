class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        #Second attempt, time O(N), space O(N)
        #Inspired by solns by SSigurd and Zeyuuuuuuu in discussion 
        ans = 0
        score = 0
        seen = {}
        for i, hour in enumerate(hours):
            score += 1 if hour > 8 else -1
            
            if score not in seen:
                seen[score] = i
            
            if score > 0:
                ans = max(ans, i+1)
            elif score-1 in seen:
                ans = max(ans, i-seen[score-1])
        return ans
        
#         #Failed recent attempt, TLE, time O(N^2), space O(N)
#         hours = [1 if hour > 8 else -1 for hour in hours]
#         prefixSum = [0]*(len(hours)+1)
        
#         for i in range(1, len(prefixSum)):
#             prefixSum[i] = prefixSum[i-1]+hours[i-1]
        
#         ans = 0
#         for j in range(1, len(prefixSum)):
#             i = 0
#             while i < j:
#                 if prefixSum[i] < prefixSum[j]:
#                     ans = max(ans, j - i)
#                     break
#                 i += 1
#         return ans
