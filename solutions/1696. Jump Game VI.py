class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        #soln 3 - Leetcode DP with deque, optimized, no score array
        n, score = len(nums), nums[0]
        dq = collections.deque([(0, score)])
        for i in range(1, n):
            while dq and dq[0][0] < i-k: # pop the old index
                dq.popleft() 
            score = dq[0][1] + nums[i]
            while dq and  dq[-1][1] <= score:
                dq.pop()
            dq.append((i, score))
        return score
    
        #soln 2 - Leetcode DP with deque
        n, score = len(nums), [0]*n
        score[0] = nums[0]
        dq = collections.deque([0])
        
        for i in range(1, n):
            while dq and dq[0] < i-k: # pop the old index
                dq.popleft() 
            score[i] = score[dq[0]] + nums[i]
            while dq and score[dq[-1]] <= score[i]: # pop the smaller value
                dq.pop() 
            dq.append(i)
        return score[-1]
    
#         #soln 1 - Jake's soln, DP with heap
#         dp = nums[0]        # highest score we can get ending at index i
#         heap = [(-dp,0)]    # Heap returns min, we want max dp, so store -dp. Keep track of index
​
#         # build initial heap of first k dp values
#         for i in range(1,min(k,len(nums))):
#             dp = nums[i] - heap[0][0]
#             heapq.heappush(heap,(-dp,i))
​
#         for i in range(k,len(nums)):
#             # if heap max is farther than k away from i, discard it
#             while i - heap[0][1] > k:
#                 heapq.heappop(heap)
#             dp = nums[i] - heap[0][0]
#             heapq.heappush(heap,(-dp,i))
#         return dp
        
#         #soln 0 - Jake's first attempt
#         for i in range(1, min(k,len(nums))):
#             nums[i] += max(nums[0:i])
        
#         for i in range(k,len(nums)):
#             nums[i] += max(nums[i-k:i])
#         return nums[-1]
