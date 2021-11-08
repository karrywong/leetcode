class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #LeetCode binary search, Time O(NlogN), Space O(1)
        l, r = 1, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            count = 0
            for n in nums:
                if n <= mid:
                    count += 1
            if count > mid:
                r = mid - 1
            else:
                l = mid + 1
        return l
        
        # #soln 2 - Leetcode recursion
        # def store(cur):
        #     if nums[cur] == cur:
        #         return cur
        #     nums[cur], temp = cur, nums[cur]
        #     return store(temp)
        # return store(0)
    
        #soln 1 - Leetcode negative marking, Time O(n), Space O(1) but in-place modification
        # ind = nums[0]
        # while nums[ind] > 0:
        #     if nums[ind] > 0:
        #         nums[ind] *= -1
        #     ind = abs(nums[ind])
        # return ind
