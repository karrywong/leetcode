class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #LeetCode, super smart, time O(N) with space O(1)
        n = len(nums)
        #First step is to check if 1 present in the array or not. If not, return 1
        if 1 not in nums:
            return 1
        
        #Second is to replace neg numbers, zeros, or numbers larger than n by 1s, output array with only pos no
        for i, num in enumerate(nums):
            if num <= 0 or num > n:
                nums[i] = 1
        
        #Key idea: use index in nums as hash key and sign of element as a hash value (presence detector).
        for i in range(n):
            a = abs(nums[i])
            if a == n:
                if nums[0] > 0:
                    nums[0] *= -1
            elif nums[a] > 0:
                nums[a] *= -1
                
        #Index of the first pos number is equal to the first missing number
        for i in range(1,n):
            if nums[i] > 0:
                return i
        
        return n if nums[0] > 0 else n+1
        
        # #First attempt, Time O(N), space O(N)
        # numSet = set(range(1, len(nums)+2))
        # for num in nums:
        #     if num in numSet:
        #         numSet.remove(num)
        # return min(numSet)
