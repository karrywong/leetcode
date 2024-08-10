class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # recent attempt, time O(N), space O(N)
        if len(nums) <= 1:
            return nums
        idx = len(nums)-2
        while idx>=0 and nums[idx] >= nums[idx+1]:
            idx -= 1
        if idx < 0:
            nums.reverse()
            return
        
        swap_idx = idx+1
        while swap_idx < len(nums) and nums[swap_idx] > nums[idx]:
            swap_idx += 1
        swap_idx -= 1
        nums[idx], nums[swap_idx] = nums[swap_idx], nums[idx]
        nums[idx+1:]=nums[idx+1:][::-1] # can be further optimized to achieve O(1) space
        return nums
    
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
            ## swap digits at i and j
            nums[i],nums[j] = nums[j],nums[i]
            # Sort the remaining digits in ascedning order
            if j < -1:
                nums[j+1:] = nums[j+1:][::-1]            
