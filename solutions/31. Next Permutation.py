class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ### Soln 1 - idea from Jake Reschke
        n = len(nums)
        if n == 1: return nums
        
        check = False
        # get index of first digit from right smaller than predecessor
        # if none return -1
        j = -2
        while nums[j] >= nums[j+1]:
            j -= 1
            if j == -n-1: 
                nums[:] = nums[::-1]
                check = True
                break
        
        if not check:
            i = -1   
            # get index of first digit from right smaller than digits[j]
            while nums[j] >= nums[i]:
                i -= 1    
​
            ## swap digits at i and j
            nums[i], nums[j] = nums[j],nums[i]
            # Sort the remaining digits in ascedning order
            if j < -1:
                nums[j+1:] = sorted(nums[j+1:])   
​
