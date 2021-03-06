class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        ### Soln 2 - sort both houses and heaters, O(max(Nlog(N), Mlog(M)))
        ### from discussion by jychstar
        houses.sort()
        heaters.sort()
        heaters=[float('-inf')]+heaters+[float('inf')] # add 2 fake heaters
        ans,i = 0,0
        for house in houses:
            while house > heaters[i+1]:  # search to put house between heaters
                i +=1
            dis = min (house - heaters[i], heaters[i+1]- house)
            ans = max(ans, dis)
        return ans
        
        
        # Soln 1 - speeded up, (M*logM + N*logM)
#         res = 0
#         n = len(heaters)
#         heaters.sort()
        
#         #find idx s.t. heaters[idx-1] < hs <= heaters[idx]
#         def bsearch(hs, heaters):
#             l, r, pos = 0, n - 1, n
#             while l <= r:
#                 mid = l + (r-l)//2
#                 if heaters[mid] >= hs:
#                     pos = mid
#                     r = mid-1
#                 else:
#                     l = mid + 1
#             return pos
        
#         for hs in houses:
#             idx = bsearch(hs, heaters)
#             if idx == n:
#                 res = max(res, hs - heaters[-1])
#             elif idx == 0:
#                 res = max(res, heaters[0] - hs)
#             else:
#                 res = max(res, min(hs - heaters[idx - 1], heaters[idx] - hs))
#         return res
​
​
