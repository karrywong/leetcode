class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        #After multiple failures, see Leetcode Two pointer, Time O(N^2), Space O(N)
        #Using selection sort instead of built-sort, Space O(1) possible
        diff, n = float('inf'), len(nums)
        nums.sort() #-4,-1,2,1
        for i in range(n-2):
            l, r = i+1, n-1
            while l < r:
                temp = nums[i] + nums[l] + nums[r]
                if abs(target - temp) < abs(diff):
                    diff = target - temp
                if diff == 0: break
                if temp < target:
                    l += 1
                else:
                    r -= 1
            if diff == 0: break
        return target - diff
