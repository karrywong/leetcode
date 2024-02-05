from collections import deque 
​
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Runtime O(N), space O(1)
        x = -1 
        deq = deque([])
        ans = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                # if k > 0 and len(deq) >= k:
                #     x = deq.popleft()
                # elif k == 0:
                #     x = i
                deq.append(i)
            if len(deq) > k:
                x = deq.popleft()
            ans = max(ans, i-x)
        return ans
    
        # ### Old attempts
        # ### Soln 2 - sliding window O(n), optimized from LeetCode solution
        # left = 0
        # for right in range(len(nums)):
        #     # If we included a zero in the window we reduce the value of K.
        #     # Since K is the maximum zeros allowed in a window.
        #     k -= 1 - nums[right]
        #     # A negative K denotes we have consumed all allowed flips and window has
        #     # more than allowed zeros, thus increment left pointer by 1 to keep the window size same.
        #     if k < 0:
        #         # If the left element to be thrown out is zero we increase K.
        #         k += 1 - nums[left]
        #         left += 1
        # return right - left + 1
        
