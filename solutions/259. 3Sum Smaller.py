class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        #soln 1 - Leetcode two pointers, fast, Time O(N^2), Space O(1)
        ans, n = 0, len(nums)
        nums.sort()
        for i in range(n-2):
            target2 = target - nums[i]
            l, r = i+1, n-1
            while l < r:
                if nums[l] + nums[r] < target2:
                    ans += r-l
                    l += 1
                else:
                    r -= 1
        return ans
        
        # #soln 0 - first attempt, two pointers, slow
        # ans, n = 0, len(nums)
        # nums.sort()
        # for i in range(n):
        #     target2 = target - nums[i]
        #     for r in range(n-1, i+1, -1):
        #         l = i+1
        #         if nums[l] + nums[r] >= target2:
        #             continue
        #         while l < r and nums[l] + nums[r] < target2:
        #             ans += 1
        #             l += 1
        # return ans
        
