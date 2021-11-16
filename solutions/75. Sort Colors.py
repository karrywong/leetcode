class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#         #soln 1 - Dutch national flag problem
#         # for all idx < p0 : nums[idx < p0] = 0
#         # curr is an index of element under consideration
#         p0 = curr = 0
#         # for all idx > p2 : nums[idx > p2] = 2
#         p2 = len(nums) - 1
​
#         while curr <= p2:
#             if nums[curr] == 0:
#                 nums[p0], nums[curr] = nums[curr], nums[p0]
#                 p0 += 1
#                 curr += 1
#             elif nums[curr] == 2:
#                 nums[curr], nums[p2] = nums[p2], nums[curr]
#                 p2 -= 1
#             else:
#                 curr += 1
​
        #counting sort
        count =  [0 for _ in range(3)]
        n = len(nums)
        output = [0 for _ in range(n)]
        # Store count of each character
        for num in nums:
            count[num] += 1
        # Change count_arr[i] so that count_arr[i] now contains actual position of this element in output array
        for i in range(1, len(count)):
            count[i] += count[i-1]
        # Build the output character array
        for i in range(n-1, -1, -1):
            output[count[nums[i]] - 1] = nums[i]
            count[nums[i]] -= 1
        # Copy the output array to arr, so that arr now contains sorted characters
        for i in range(n):
            nums[i] = output[i]   
                
#         #soln 0 - Jake's solution
#         i,j,k = 0,0,len(nums) - 1
#         while j <= k:
#             if nums[j] == 0:
#                 nums[i],nums[j] = 0,nums[i]
#                 i += 1
#             elif nums[j] == 2:
#                 nums[j],nums[k] = nums[k], 2
#                 k -= 1
            
#             if j < i or nums[j] == 1:
#                 j += 1
