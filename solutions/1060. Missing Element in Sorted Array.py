class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        #LeetCode binary search, even faster, time O(logN), space O(1):
        missing = lambda idx: nums[idx] - nums[0] - idx
        
        n = len(nums)
        if k > missing(n-1):
            return nums[n-1]+k-missing(n-1)
        
        l, r = 0, n-1 #Binary search
        while l < r:
            mid = l + (r-l)//2
            if missing(mid) < k:
                l = mid+1
            else:
                r = mid
        return nums[l-1]+k-missing(l-1) 
        
        # #LeetCode one-pass, super clever, time O(N), space O(1), 
        # #similar but easier than problem 41. First Missing Positive
        # # Return how many numbers are missing until nums[idx]
        # missing = lambda idx: nums[idx] - nums[0] - idx
        # n = len(nums)
        # i = 1
        # while i < n and missing(i) < k:
        #     i += 1
        # return nums[i-1] + k - missing(i-1) 
        
        # #LTE, time O(R*log(k)+N), where R = len(range(nums[0], nums[-1]+k+1)) and N = len(nums), space O(R)
        # numSet = set(range(nums[0], nums[-1]+k+1))
        # for num in nums:
        #     numSet.remove(num)
        # return heapq.nsmallest(k,numSet)[-1]
