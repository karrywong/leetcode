class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        #LeetCode soln - sorting + max/min, super clever, time O(NlogN), space O(N)
        nums.sort()
        ans = nums[-1] - nums[0]
        mi_bd, ma_bd = nums[0]+k, nums[-1]-k
        
        for i in range(len(nums)-1):
            a, b = nums[i], nums[i+1]
            ans = min(ans, max(ma_bd, a+k) - min(mi_bd, b-k))
            
        return ans
​
        # #soln by lee215, time O(NlogN), space O(N)
        # ma, mi = max(nums), min(nums)
        # if ma - mi >= 4 * k: return ma - mi - 2 * k
        # if ma - mi <= k: return ma - mi
        # inter = sorted([i for i in nums if ma - 2 * k < i < mi + 2 * k] + [ma - 2 * k, mi + 2 * k])
        # return min(a + 2 * k - b for a, b in zip(inter, inter[1:]))
