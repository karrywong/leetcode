class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # # recent, attempt time O(N), space O(N)
        # prefix_sum = [0]
        # for num in nums:
        #     prefix_sum.append(num + prefix_sum[-1])
        # left = 0
        # ans = len(nums)+1
        # for right, psum in enumerate(prefix_sum):
        #     if right == 0:
        #         continue
        #     val = psum - prefix_sum[left]
        #     if val >= target:
        #         while val >= target:
        #             left += 1
        #             val = psum - prefix_sum[left]
        #         left -= 1
        #         ans = min(ans, right-left)
        # return ans if ans < len(nums)+1 else 0
​
        #Leetcode, prefix sum + sliding window, much cleaner
        # time O(N), space O(1)
        n, ans = len(nums), float('inf')
        j, cur_sum = 0, 0
        for i in range(n):
            cur_sum += nums[i]
            while cur_sum >= target:
                ans = min(ans, i-j+1)
                cur_sum -= nums[j]
                j += 1
        return 0 if ans == float('inf') else ans
                
            
                
            
        
            
