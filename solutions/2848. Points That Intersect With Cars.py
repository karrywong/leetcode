class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort()
        ans, end = 0, 0
        for s, e in nums:
            if end >= s:
                ans += max(e - end,0)
            else: # end <= s
                ans += e-s+1
            end = max(e,end)
        return ans
                
