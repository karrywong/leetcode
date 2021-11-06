class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        #soln 2 - Leetcode PrefixSum, modified from 3. Longest Substring Without Repeating Characters
        m = len(nums)
        lastIndexes, l, ans = [-1]*10001, 0, 0 #lastIndexes replaces map
        prefixSum = [0] * (m+1)
        for r, n in enumerate(nums):
            prefixSum[r+1] = prefixSum[r] + n
            if lastIndexes[n] != -1 and l <= lastIndexes[n]:
                l = lastIndexes[n] + 1
            ans = max(ans, prefixSum[r+1] - prefixSum[l])
            lastIndexes[n] = r 
        return ans
        
        # #soln 1 - Leetcode, two pointers + sliding window
        # #Worst case, visit every number twice
        # l = 0
        # isPresent = [False] * 10001 #replace set to keep track of seen numbers
        # ans, cur_sum = 0, 0
        # for n in nums:
        #     while isPresent[n]:
        #         isPresent[nums[l]] = False
        #         cur_sum -= nums[l]
        #         l += 1
        #     cur_sum += n
        #     isPresent[n] = True
        #     ans = max(ans, cur_sum)
        # return ans
        
​
        
