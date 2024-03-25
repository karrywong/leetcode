class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #  0 1 2 3 4
        # [1,3,4,2,2]
        # [1,3,2,1,4], cur=3 -> ans = 2
        
        # [3,1,3,4,2]
        # [3,1,2,3,4], cur=3 -> ans = 3
        
        # 1,2,3,.., n
        # number i should have i as index
        
        # cur = nums[0]
        # cnt = 0
        # while cur != nums[cur]:  
        #     nums[cur], cur = cur, nums[cur] 
        #     # temp = nums[cur]
        #     # nums[cur] = cur
        #     # cur = temp
        # return cur
​
        #soln 1 - Leetcode negative marking, Time O(n), Space O(1) but in-place modification
        # ind = nums[0]
        # while nums[ind] > 0:
        #     if nums[ind] > 0:
        #         nums[ind] *= -1
        #     ind = abs(nums[ind])
        # return ind
    
        #LeetCode binary search, Time O(NlogN), Space O(1)
        l, r = 1, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            count = 0
            for n in nums:
                if n <= mid:
                    count += 1
            if count > mid:
                duplicate = mid
                r = mid - 1
            else: #count <= mid
                l = mid + 1
        return duplicate
