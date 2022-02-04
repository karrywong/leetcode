class Solution:
    def rob(self, nums: List[int]) -> int:
        #Second attempt, same idea but cleaner, time O(N), space O(1)
        if len(nums) <= 3: return max(nums)
        def rob_alg(lst):
            n = len(lst)
            RobNextNext = 0
            RobNext = lst[n-1]
            for i in range(n-2,-1,-1):
                current = max(RobNext, RobNextNext + lst[i])
                RobNextNext = RobNext
                RobNext = current
            return current
        return max(rob_alg(nums[1:]), rob_alg(nums[:-1]))
            
#         #First attempt, reduced to 198. House Robber
#         n = len(nums)
#         if n <= 3: return max(nums)
        
#         rob1 = nums[:n-1] #length of n-1
#         rob1[2] += rob1[0]
#         for i in range(3,n-1):
#             rob1[i] += max(rob1[i-2], rob1[i-3])
#         ans1 = max(rob1[-1], rob1[-2])
        
#         rob2 = nums[1:]
#         rob2[2] += rob2[0]
#         for i in range(3,n-1):
#             rob2[i] += max(rob2[i-2], rob2[i-3])
#         ans2 = max(rob2[-1], rob2[-2])   
#         return max(ans1, ans2)
        
