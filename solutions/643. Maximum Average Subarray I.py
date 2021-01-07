class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ### Soln 1 - sliding window
        temp_sum = sum(nums[:k])
        res = temp_sum 
        for i in range(k, len(nums)):
            temp_sum += nums[i] - nums[i-k]
            res = max(res, temp_sum)
        return res/k
        
            
                
​
​
