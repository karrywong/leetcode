class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        #first attempt, prefix product + sliding windows
        n, ans = len(nums), 0
        j, cur_prod = 0, 1
        for i in range(n):
            cur_prod *= nums[i]                
            while j <= i and cur_prod >= k:
                cur_prod /= nums[j]
                j += 1
            ans += i-j+1
        return ans
            
            
        
