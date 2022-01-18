class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Time O(N), space O(N)
        #Modified Jake's solution for 556. Next Greater Element III
        n = len(nums)
        if n == 1: return nums
        # get index of first digit from right smaller than predecessor, return -1 if none
        j = -2
        while j > -n-1 and nums[j] >= nums[j+1]:
            j -= 1
        if j == -n-1: 
            nums.reverse()
        else:
            # get index of first digit from right larger than digits[j]
            i = -1  
            while nums[j] >= nums[i]:
                i -= 1
​
            ## swap digits at i and j
            nums[i],nums[j] = nums[j],nums[i]
            # Sort the remaining digits in ascedning order
            if j < -1:
                nums[j+1:] = nums[j+1:][::-1]            
