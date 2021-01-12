​
        # get first window
​
        for x in nums[1 : k]:
            winQueue.append(x)
            while maxDeque and x > maxDeque[0]:
                maxDeque.popleft()
            maxDeque.appendleft(x)
​
        winMax = [maxDeque[-1]]
​
        for x in nums[k : ]:
            if winQueue.popleft() == maxDeque[-1]:
                maxDeque.pop()
​
            winQueue.append(x)
​
            while maxDeque and x > maxDeque[0]:
                maxDeque.popleft()
            maxDeque.appendleft(x)
​
            winMax.append(maxDeque[-1])
​
        return winMax
​
​
#         ### Soln 2 - deque (double-ended queue) O(N), LeetCode solution
#         # base cases
#         n = len(nums)
#         if n * k == 0: return []
#         if k == 1: return nums
        
#         def clean_deque(i):
#             # remove indexes of elements not from sliding window
#             if deq and deq[0] == i - k:
#                 deq.popleft()
                
#             # remove from deq indexes of all elements 
#             # which are smaller than current element nums[i]
#             while deq and nums[i] > nums[deq[-1]]:
#                 deq.pop()
        
#         # init deque and output
#         deq = collections.deque()
#         max_idx = 0
#         for i in range(k):
