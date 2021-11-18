class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #Attempt with just ordinary library
        seen = {}
        cur_sum, count = 0,0
        for n in nums:
            cur_sum += n
            if cur_sum == k:
                count += 1
            if cur_sum - k in seen:
                count += seen[cur_sum-k]
            
            if cur_sum in seen:
                seen[cur_sum] += 1
            else:
                seen[cur_sum] = 1
        return count
        
        #Leetcode prefix sum, Time O(N), Space O(N)
        #More challenging, 437. Path Sum III
        # lib = collections.defaultdict(int)
        # cur_sum, count = 0, 0
        # for n in nums:
        #     cur_sum += n            
        #     #situation 1: prefix sum equal targetSum
        #     if cur_sum == k: 
        #         count += 1
        #     #situation 2: subarray starting in middle equal targetSum
        #     #proof: cur_sum - (cur_sum - target) = target
        #     count += lib[cur_sum - k]
        #     #update
        #     lib[cur_sum] += 1
        # return count
