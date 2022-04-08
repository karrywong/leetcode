class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        #Tricky, Leetcode's soln, using prefix Sum plus hashset
        #Time O(N^2), space O(N)
        n = len(nums)
        if n < 7:
            return False
        prefixSum = [nums[0]]
        for i in range(1, n):
            prefixSum.append(prefixSum[-1]+nums[i])
                
        for j in range(3, n-3):
            htb = set()
            for i in range(1,j-1):
                if prefixSum[i-1] == prefixSum[j-1]-prefixSum[i]:
                    htb.add(prefixSum[i-1])
    
            for k in range(j+2,n-1):
                last_quarter_sum = prefixSum[k-1] - prefixSum[j]
                if prefixSum[n-1]-prefixSum[k] == last_quarter_sum and last_quarter_sum in htb:
                    return True
        return False
