class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #soln 1 - LeetCode Greedy
        n = len(nums)
        lastPos = n - 1
        for i in range(n-2,-1,-1):
            if i + nums[i] >= lastPos:
                lastPos = i
        return lastPos == 0
        
        # #soln 0 - first attempt by Jake, Time O(n), Space O(1)
        # jump = False
        # j = 0
        # for i in range(len(nums)-2,-1,-1):
        #     if not jump and nums[i] > 0:
        #         continue
        #     elif not jump and nums[i] == 0:
        #         jump = True
        #         j = 0
        #     else:
        #         j += 1
        #         if nums[i] > j:
        #             jump = False
        # return not jump
​
