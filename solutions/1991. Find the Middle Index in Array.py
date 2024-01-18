class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i == 0:
                leftSum, rightSum = 0, sum(nums[1:])
            else:  
                leftSum += nums[i-1]
                rightSum -= nums[i]
                
            if leftSum == rightSum: 
                return i
        return -1
            
