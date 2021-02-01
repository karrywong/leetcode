class Solution:
    def maximumSwap(self, num: int) -> int:
        ### Soln 0 - first attempt, similar to Next Permutation
        nums = [int(x) for x in str(num)]
        if all(nums[i-1] >= nums[i] for i in reversed(range(1, len(nums)))):
            return num
        i = 0
        while nums[i] >= max(nums[i+1:]):
            i += 1
        idx = ~nums[::-1].index(max(nums[i+1:]))
        
        nums[i], nums[idx] = nums[idx], nums[i]
​
        return int(''.join(map(str,nums)))
        
        
        
        
        
        
