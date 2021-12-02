class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Second attempt, time O(N), space O(1)
        n = len(nums)
        ans, val = [1]*n, 1
        for i in range(1,n):
            val *= nums[i-1]
            ans[i] *= val
        val = 1
        for i in range(n-1, 0, -1):
            val *= nums[i]
            ans[i-1] *= val
        return ans
        
        # #First attempt, products from left to right and from right to left, time O(N), space O(N)
        # n = len(nums)
        # prodlr = [0] * (n-1)
        # prodrl = [0] * (n-1)
        # prodlr[0], prodrl[-1] = nums[0], nums[-1]
        # for i in range(1,n-1):
        #     prodlr[i] = prodlr[i-1]*nums[i] #i=0,1,..,n-2
        #     prodrl[~i] = prodrl[~i+1]*nums[~i] #i=-2,-3,...,-n+1
        # ans = [prodrl[0]] + [prodrl[i]*prodlr[i-1] for i in range(1,n-1)] + [prodlr[n-2]]
        # return ans
