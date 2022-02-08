class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        #Time O(N), space O(1), soln by lee215 with idea from @ye15
        #answer can only be the last house with different color of the fisrt house.
        #or the first house with different color of the last house
        ans = 0
        for i, x in enumerate(colors):
            if x != colors[0]:
                ans = max(ans, i)
            if x != colors[-1]:
                ans = max(ans, len(colors)-1-i)
        return ans
        
        #First attempt, Time O(N^2), spacee O(N)
        #To be optimized
#         lib = collections.defaultdict(list)
#         for i, color in enumerate(colors):
#             lib[color].append(i)
        
#         ans = float('-inf')
#         lst = list(lib.values())
#         n = len(lst)
#         for i in range(n):
#             for idx in lst[i]:
#                 for j in range(i+1,n):
#                     for idy in lst[j]:
#                         ans = max(ans, abs(idx-idy))
#         return ans
