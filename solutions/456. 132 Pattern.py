class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        #Leetcode stack, inspired from search interval, time O(N), space O(N)
        min_pts = [nums[0]]+[None]*(len(nums)-1)
        for i in range(1,len(nums)):
            min_pts[i] = min(nums[i], min_pts[i-1])
​
        stack = []
        for j in range(len(nums)-1, -1, -1):
            if nums[j] == min_pts[j]:
                continue
            while stack and stack[-1] <= min_pts[j]:
                stack.pop()
            if  stack and stack[-1] < nums[j]:
                return True
            stack.append(nums[j])
        return False                              
            
        # #Leetcode search interval, time O(N^2), space O(N)
        # intervals = []
        # min_pt_after_last_peak_index = 0
        # for i in range(len(nums)):
        #     if nums[i] < nums[i-1]:
        #         if min_pt_after_last_peak_index < i-1:
        #             intervals.append((nums[min_pt_after_last_peak_index], nums[i-1]))
        #         min_pt_after_last_peak_index = i
        #     for interval in intervals:
        #         if interval[0] < nums[i] < interval[1]:
        #             return True
        # return False
        
        # #Leetcode better brute force, time O(N^2), space O(1)
        # min_i = float('inf')
        # for j in range(len(nums)-1):
        #     min_i = min(min_i, nums[j])
        #     for k in range(j+1, len(nums)):
        #         if min_i < nums[k] < nums[j]:
        #             return True
        # return False
        
        # #Leetcode brute force, time O(N^3), space O(1)
        # for i in range(len(nums)-2):
        #     for j in range(i+1, len(nums)-1):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] < nums[k] < nums[j]:
        #                 return True
        # return False
