class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        # Soln 1 - Two pointers + sort, O(nlogn)
#         nums.sort()
#         right = len(nums) - 1
#         left = 0
#         res = -1
        
#         while left < right:
#             temp = nums[right] + nums[left]
#             if temp >= k:
#                 right -= 1
#             else:
#                 res = max(res, temp)
#                 left += 1
        
#         return res
​
        # Soln 2 - Two pointers, without sort O(n + m)
        answer = -1
        count = [0] * 1001
        for num in nums:
            count[num] += 1
        lo = 1
        hi = 1000
        while lo <= hi:
            if lo + hi >= k or count[hi] == 0:
                hi -= 1
            else:
                if count[lo] > (0 if lo < hi else 1):
                    answer = max(answer, lo + hi)
                lo += 1
        return answer
