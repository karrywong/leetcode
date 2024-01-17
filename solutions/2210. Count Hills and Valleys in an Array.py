class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        nums2 = []
        for i in range(len(nums)):
            if i == 0 or nums[i] != seen:
                nums2.append(nums[i])
                seen = nums[i]
        ans = 0
        for i in range(1, len(nums2)-1):
            left, right = nums2[i-1], nums2[i+1]
            if (left > nums2[i] and nums2[i] < right) or (left < nums2[i] and nums2[i] > right):
                ans += 1
        return ans
        
        #[3,3,3,4,4,3,3] -> [3,4,3] ans = 1
        #[2,4,1,1,6,5] -> [2,4,1,6,5], ans = 3
        # [6,5,4,1] -> []
        
        #(i,j,ans), (2,0,1), (3,-1,1), (4,0,2), (5,0,3)
        
#         for num in nums[2:]:
#             if num != nums[i-1]:
#                 prevprev, prev = nums[i-j-2], nums[i-j-1]
#                 j = 0
#             else:
#                 j -= 1
#                 continue
                
#             if (prevprev < prev and prev > num) or (prevprev > prev and prev < num):
#                 ans += 1
                
#             i += 1
#         return ans
