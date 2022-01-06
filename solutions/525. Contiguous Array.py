class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        #Brute force: check every possible subarray, time O(N^2), space O(1)
        # #1. LeetCode extra array, time O(N), space O(1)
        # n = len(nums)
        # arr = [-2]*n + [-1] + [-2]*n
        # ans, count = 0, 0 
        # for i, num in enumerate(nums):
        #     count = count+1 if num else count-1
        #     if arr[count+n] >= -1:
        #         ans = max(ans, i-arr[count+n])
        #     else:
        #         arr[count+n] = i
        # return ans
        
        #LeetCode hashtable, time O(N), space O(1)
        htb = {0:-1}
        ans, count = 0, 0 
        for i, num in enumerate(nums):
            count = count+1 if num else count-1
            if count in htb:
                ans = max(ans, i-htb[count])
            else:
                htb[count] = i
        return ans
