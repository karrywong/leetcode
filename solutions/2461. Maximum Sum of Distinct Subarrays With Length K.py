from collections import Counter
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        seen = Counter(nums[:k]) #unordered_map
        val = sum(nums[:k])
        duplicate = set() #unordered_set
        if len(seen) < k:
            ans = 0
            duplicate.update([s for s in seen if seen[s] > 1])
        else:
            ans = val
        
        # [1,1,1,2,3]
        for i in range(k, len(nums)):
            seen[nums[i-k]] -= 1
            if nums[i-k] in duplicate and seen[nums[i-k]] <= 1:
                duplicate.remove(nums[i-k])
                
            seen[nums[i]] += 1
            if seen[nums[i]] > 1:
                duplicate.add(nums[i])
            
            val -= nums[i-k]
            val += nums[i]
            
            if len(duplicate) == 0: ans = max(ans,val)
        
        return ans
