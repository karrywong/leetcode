from collections import defaultdict
​
​
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Two ideas:
        # cur_sum == target, ans += 1
        # bookkeep # occurence of cur_sum
        # if cur_sum-target in lookup, cur_sum - (cur_sum-target) = target
        # ans += lookup[cur_sum-target]
        
        # brute-force, compute all possible subarray, time: O(N^3), space O(1)
        
        # Time O(N), space O(N), N = len(nums)
        ans = cur_sum = 0
        lookup = defaultdict(int)
        for num in nums:
            cur_sum += num
            if cur_sum == k:
                ans += 1
                
            ans += lookup[cur_sum-k]
            lookup[cur_sum] += 1
        return ans
    
    # [3,2,1], target = 3
    # a = 1, cur_sum = 6, ans = 1
    # ans += lookup[3]
    # {3:1, 5:1, 6:1}
    
    # [1,1,1], target = 2
    #      | 
    # ans = 2, cur_sum = 3
    # lookup = {1:1, 2:1, 3:1}
            
        
        
