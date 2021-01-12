class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:        
        ### Soln 2 - deque (double-ended queue) O(N), LeetCode solution
        # base cases
        n = len(nums)
        if n * k == 0: return []
        if k == 1: return nums
        
        def clean_deque(i):
            # remove indexes of elements not from sliding window
            if deq and deq[0] == i - k:
                deq.popleft()
                
            # remove from deq indexes of all elements 
            # which are smaller than current element nums[i]
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()
        
        # init deque and output
        deq = collections.deque()
        max_idx = 0
        for i in range(k):
            clean_deque(i)
            deq.append(i)
            # compute max in nums[:k]
            if nums[i] > nums[max_idx]:
                max_idx = i
        output = [nums[max_idx]]
        
        # build output
        for i in range(k, n):
            clean_deque(i)          
            deq.append(i)
            output.append(nums[deq[0]])
        return output
    
        ### Soln 1 - brute force O(N * k), time exceeded 
#         if k == 1: return nums 
#         elif k == len(nums): return [max(nums)]
        
#         window = [] #k >= 2
#         res = []
#         for n in nums:
#             if len(window) < k:
#                 window.append(n)
#             else:
#                 window.append(n)
#                 window.pop(0)
#             if len(window) == k:
#                 res.append(max(window))
#         return res
