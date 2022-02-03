class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #soln 0 - DP with deque, similar to 1696. Jump Game VI
        #Time O(N), space O(N)
        n, ans = len(nums), []
        dq = collections.deque(sorted([(i, v) for i, v in enumerate(nums[0:k])], key=lambda x:x[1], reverse = True))
​
        ans.append(dq[0][1])
        for i in range(k, n):
            while dq and dq[0][0] <= i-k: # pop the old index
                dq.popleft() 
            while dq and  dq[-1][1] <= nums[i]:
                dq.pop()
            dq.append((i, nums[i]))
            ans.append(dq[0][1])
        return ans
​
