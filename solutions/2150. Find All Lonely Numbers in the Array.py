class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        #Second attempt, time O(N), space O(N)
        #Inspired by Silvia42, idea is to use Counter
        ans = []
        counts = collections.Counter(nums)
        for num, freq in counts.items():
            if freq + counts[num-1] + counts[num+1] == 1:
                ans.append(num)
        return ans
        
#         #First attempt, time O(N), space O(N)
#         ans = set()
#         seen = set()
#         i = 0
        
#         while i < len(nums):
#             bo = True
#             if nums[i] in ans:
#                 ans.remove(nums[i])
#                 bo = False
#             if nums[i]+1 in seen and nums[i]+1 in ans:
#                 ans.remove(nums[i]+1)
#                 bo = False
#             if nums[i]-1 in seen and nums[i]-1 in ans:
#                 ans.remove(nums[i]-1)
#                 bo = False
            
#             if bo and nums[i] not in seen and nums[i]-1 not in seen and nums[i]+1 not in seen:
#                 ans.add(nums[i])
#             seen.add(nums[i])
#             i += 1
​
#         return list(ans)
​
