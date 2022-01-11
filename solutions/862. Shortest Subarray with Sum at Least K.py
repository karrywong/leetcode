class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        #brute force: sum(nCk * (n-k+1)) over k = 1,..,n ~ O(n * 2^n)
        #eg, nums = [1,2,-1,4,1], k = 5
        
        # #idea: prefix sum + sliding window
        # #solution by WangQiuc in discussion
        # #Time O(N), space O(N)
        n = len(nums)
        queue = collections.deque([(-1,0)])
        ans = n+1
        prefix_sum = 0
        for i, num in enumerate(nums):
            prefix_sum += num
            if num > 0:
                while queue and prefix_sum - queue[0][1] >= k:
                    ans = min(ans, i - queue.popleft()[0])
            else:
                while queue and prefix_sum <= queue[-1][1]:
                    queue.pop()
            queue.append((i, prefix_sum))
        return ans if ans < n+1 else -1
    
#         #Similar Leetcode prefix sum + sliding window, Time O(N), space O(N)
#         N = len(A)
#         P = [0]
#         for x in A:
#             P.append(P[-1] + x)
​
#         #Want smallest y-x with Py - Px >= K
#         ans = N+1 # N+1 is impossible
#         monoq = collections.deque() #opt(y) candidates, represented as indices of P
#         for y, Py in enumerate(P):
#             #Want opt(y) = largest x with Px <= Py - K
#             while monoq and Py <= P[monoq[-1]]:
#                 monoq.pop()
​
#             while monoq and Py - P[monoq[0]] >= K:
#                 ans = min(ans, y - monoq.popleft())
​
#             monoq.append(y)
​
#         return ans if ans < N+1 else -1
