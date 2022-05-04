class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = n, 0
        stack = []
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] > num: #when there is a failling slope
                l = min(l, stack.pop())
            stack.append(i)
            
        stack = []
        for i, num in enumerate(nums[::-1]):
            i = n-1-i
            while stack and nums[stack[-1]] < num: #when there is a rising slope
                r = max(r,stack.pop())
            stack.append(i)
        return r - l + 1 if r > l else 0
        
        # #First attempt, time O(NlogN), space O(1)
        # nums_ref = sorted(nums)
        # indices = [None, None]
        # for i, pairs in enumerate(zip(nums, nums_ref)):
        #     if pairs[0] != pairs[1]:
        #         if indices[0] is None:
        #             indices[0] = i
        #         else:
        #             indices[1] = i
        # return indices[1]-indices[0]+1 if indices[1] is not None else 0
