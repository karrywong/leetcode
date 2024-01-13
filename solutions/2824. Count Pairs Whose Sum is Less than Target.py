class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
       # [-1,1,1,2,3] <- [0,1,4,2,3]
       # (-1,3) -> (-1,2) -> (1,2) -> (-1,1) -> (-1,1)
       # ans = 3
    
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] < target:
                    ans += 1
        return ans
    
    # sorted array, [-7,-6,-2,-1,2,3,5], target = -2
    # i = 0, j = 6
    # (-7,5) -> (-7,3), ans = 1 -> ... -> (-6,3), ans = 2
    
    # [], target = 100, i=0 -> 6, j = 6
    # 7 * 6 / 2 = 28 = 1 + ... + 7
    # ans = 7
    
#     #[0,1,2] = n*(n-1)//2
    
#     i, j = 0, len(nums)-1
#     ans = 0
#     while i < j: 
#         val = nums[i] + nums[j]
#         if val >= target:
#             j -= 1
#         else: # val < target
#             ans += j-i
#             i += 1
            
#     return ans
        
​
    
