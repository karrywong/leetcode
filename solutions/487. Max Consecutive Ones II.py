class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int: 
        # 1004. Max Consecutive Ones III, runtime O(N), space O(1)
        k, ans = -1, 0
        deq = deque([])
        for i in range(len(nums)):
            if nums[i] == 0:
                deq.append(i)
            if len(deq) > 1:
                k = deq.popleft()
            ans = max(ans, i-k)
        return ans
        
#         # two pointer, Runtime O(N), space O(1)
#         k = -1 
#         j = 0 # last seen 0 position
#         cnt_zero = 0
#         ans = 0
        
#         for i in range(len(nums)):
#             if nums[i] == 0:
#                 cnt_zero += 1
#                 if cnt_zero > 1:
#                     k = j
#                 j = i
#             ans = max(ans, i-k)
#         return ans
    
    #  (i, k, j, ans)
    # [1,0,1,1,0] 
    # (0, -1, 0, 1) -> (1, -1, 1, 2) -> (2,-1,1,3) -> (3,-1,1,4) -> (4,1,4,4)
