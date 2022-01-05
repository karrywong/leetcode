class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #solution 1 - time: O(nums.length), memory: O(nums.length)
        #return set(range(1,len(nums)+1)) - set(nums)
        
        #solution 2 - time: O(nums.length^2), memory: O(1) - too slow
        #return [x for x in range(1, len(nums)+1) if x not in nums]   
        
#         #solution 3 - modify in place 
#         #time: O(nlogn) with n = nums.length, memory: O(1)
#         nums.sort() 
#         n = len(nums)
#         ans = []
        
#         while nums:
#             ele = nums.pop()
#             if ele < n:
#                 ans += [i for i in range(ele+1, n+1)]    
#             n = ele - 1    
#         if n != 0:
#             ans += list(range(1, count+1))
#         return ans
​
        #solution 4 - Leetcode negative marking, time: O(N), memory: O(1) 
        for i in range(0,len(nums)):
            if nums[abs(nums[i])-1] > 0:
                nums[abs(nums[i])-1] *= -1
        ans = []
        for i in range(0,len(nums)):
            if nums[i] > 0:
                ans.append(i+1)
        return ans 
