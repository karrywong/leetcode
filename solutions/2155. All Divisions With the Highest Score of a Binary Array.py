class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        #Coding contest, first attempt, DP approach and count consecutive zeros and ones
        #Time O(N), space O(N)
        zeros = [0] * (len(nums)+1)
        ones = [0] * (len(nums)+1)
        
        for i in range(len(nums)):
            zeros[i+1] = zeros[i]+1 if nums[i] == 0 else zeros[i]
        for i in range(len(nums)-1,-1,-1):
            ones[i] = ones[i+1]+1 if nums[i] == 1 else ones[i+1]
        
        vec = [z+o for z,o in zip(zeros, ones)]
        maxval = max(vec)
        ans = []
        for i, v in enumerate(vec):
            if v == maxval:
                ans.append(i)
        return ans
            
