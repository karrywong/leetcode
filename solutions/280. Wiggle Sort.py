class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #second attempt, Jake's one-liner
        f = lambda x,y,b: x > y if b == 1 else x < y
        n = len(nums)
        if n == 1: return nums
        for i in range(1, n):
            if f(nums[i-1],nums[i],i%2):
                nums[i-1], nums[i] = nums[i], nums[i-1]
            
        # #first attempt, clumsy
        # n = len(nums)
        # if n == 1: return nums
        # for i in range(1, n):
        #     if i%2 == 1:
        #         if nums[i-1] > nums[i]:
        #             nums[i-1], nums[i] = nums[i], nums[i-1]
        #     else: #i%2 == 0
        #         if nums[i-1] < nums[i]:
        #             nums[i-1], nums[i] = nums[i], nums[i-1]
                
