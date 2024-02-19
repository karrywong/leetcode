class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # Two pointers, O(NlogN), space O(1)
        nums.sort()
        left, right = 0, len(nums)-1
        ans = 0
        num_max = 10**9+7
        while left <= right:
            if (nums[left] + nums[right] <= target):
                ans += pow(2,right-left,num_max)
                left += 1
            else:
                right -= 1
        return ans % num_max
                
        # Time binary search, time O(NlogN), space O(1)
        nums.sort()
        ans = 0
        num_max = 10**9+7
        #given i, find largest j such nums[i] + nums[j] <= target
        for i in range(len(nums)):
            if nums[i] + nums[i] > target:
                break
            l, r = i, len(nums)
            while l < r:
                mid = l + (r-l) // 2
                if (nums[i] + nums[mid] <= target):
                    l = mid + 1
                else:
                    r = mid
            ans += pow(2,l-i-1,num_max)
        return ans % num_max
​
#  nums = [3,5,6,7], t = 9
# i=0, (0,4) -> (2,3) -> (3,3) , l=3, ans += 4
​
# nums = [3,3,6,8], t = 10
# i=0, (0,4)->(3,4)->(3,3), l = 3, ans = +4
# i=1, (1,4)->(3,4), l = 3, ans = +=2 
​
#         # Time O(N^2), space O(1)
#         nums.sort()
#         ans = 0
#         for i in range(len(nums)):
#             if nums[i] + nums[i] > target:
#                 break
#             for j in range(i, len(nums)):
#                 val = nums[i] + nums[j]
#                 if val > target:
#                     break
#                 if i == j:
#                     ans += 1
#                 else:
#                     ans += 2**(j-i-1)
                
#         return ans % (10**9+7)
