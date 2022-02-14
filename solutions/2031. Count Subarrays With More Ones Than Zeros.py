class Solution:
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        #Failed attempts with right idea of prefixSum, soln by newbiecoder1
        #Time O(N), space O(N)
        prefixSum = collections.defaultdict(int)
        prefixSum[0] = 1
        val = 0
        count = 0
        ans = 0
        modval = 10**9 + 7
        for num in nums:
            if num == 1:
                val += 1
                #any subarray ending at i-1 and has sum = 0 will create a new valid subarray
                count += prefixSum[val-1] 
            else:
                val -= 1
                #any subarray ending at i-1 and has sum = 1 will become invalid.
                count -= prefixSum[val]
            ans += count 
            prefixSum[val] += 1
            ans %= modval
        return ans 
