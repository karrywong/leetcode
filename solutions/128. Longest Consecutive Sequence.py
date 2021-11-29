class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Had the same idea as Leetcode set method, but could not argue that time complexity is O(N)
        n = len(nums)
        if n <= 1: return n
        nums_set = set(nums)
        ans = 1
        
        for num in nums: #O(n)
            if num - 1 not in nums_set: 
                count = 1
                while num + 1 in nums_set: #while loop can only run for n iterations throughout entire algorithm
                    num += 1
                    count += 1
                ans = max(count, ans)
        return ans
        
        # #Soln by Jake Reschke using Hashtable, O(N) time complexity, O(N) space complexity
        # d = dict()
        # ans = 0
        # for x in nums:
        #     if x in d:
        #         continue
        #     else:
        #         d[x] = None
        #         right = 0 if x + 1 not in d else d[x + 1]
        #         left = 0 if x - 1 not in d else d[x - 1]
        #         curLen = right + left + 1
        #         d[x + right] = d[x - left] = curLen
        #         ans = max(ans, curLen)
        # return ans
