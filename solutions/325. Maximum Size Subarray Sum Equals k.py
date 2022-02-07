class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        #Optimize first attempt, Time O(N), Space O(N)
        seen, ans = {}, 0
        cur_sum = 0
        
        for i, num in enumerate(nums):
            cur_sum += num
            if cur_sum == k:
                ans = i+1
            if cur_sum - k in seen:
                ans = max(ans, i-seen[cur_sum-k])
            if cur_sum not in seen:
                seen[cur_sum] = i
        return ans
    
        # #First attempt, prefix sum + hash map, Time O(N), Space O(N)
        # seen, ans = collections.defaultdict(list), 0
        # n, cur_sum = len(nums), 0
        # for i, num in enumerate(nums):
        #     cur_sum += num
        #     if cur_sum == k:
        #         ans = max(ans, i+1)
        #     for j in seen[cur_sum-k]:
        #         ans = max(ans, i - j)
        #     seen[cur_sum].append(i)
        # return ans
        
