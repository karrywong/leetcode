class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """        
        #second attempt, sort, Time O(NlogN)
        n, s = len(nums), sorted(nums)
        m = n//2+n%2
        nums[::2] = s[:m][::-1] #smallest numbers in descending order in even indices
        nums[1::2] = s[m:][::-1] #largest numbers in descending order in odd indices
            
        # #first attempt, failed!!! Example: [5,5,4,4], answer should be [4,5,4,5]
        # n = len(nums)
        # if n == 1: return nums
        # for i in range(1, n):
        #     if i%2 == 1:
        #         if nums[i-1] >= nums[i]:
        #             nums[i-1], nums[i] = nums[i], nums[i-1]
        #     else: #i%2 == 0
        #         if nums[i-1] <= nums[i]:
        #             nums[i-1], nums[i] = nums[i], nums[i-1]
                
        
