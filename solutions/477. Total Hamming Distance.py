class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        #one-liner by Stefan Pochmann
        # return sum(b.count('1')*b.count('0') for b in zip(*map('{:032b}'.format, nums)))
        
        #First attempt, counting ones and zeros
        #Time O(log(max_num) * len(num)), space O(1)
        n = len(nums)
        ones, zeros, ans = 0,0,0
        while sum(nums) != 0:
            for i in range(n):
                if nums[i] % 2 == 0:
                    zeros += 1
                else:
                    ones += 1
                nums[i] >>= 1
            if zeros != 0 and ones != 0:
                ans += zeros*ones
            ones, zeros = 0,0
        return ans
