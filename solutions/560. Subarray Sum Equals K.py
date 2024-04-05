from collections import defaultdict
​
​
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #time O(N), space O(N)
        lib = defaultdict(int)
        ans, cur_sum = 0, 0
        
        for num in nums:
            cur_sum += num
            #situation 1: prefix sum equal targetSum
            if cur_sum == k:
                ans += 1
            #situation 2: subarray starting in middle equal targetSum
            #proof: cur_sum - (cur_sum - target) = target
            ans += lib[cur_sum-k]
            #update
            lib[cur_sum] += 1
        return ans
