class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        # #Better brute force, time O(N^2), space(1)
        # ans = 0
        # for i in range(len(nums)):
        #     mi, ma = nums[i], nums[i]
        #     for j in range(i+1, len(nums)):
        #         mi = min(nums[j],mi)
        #         ma = max(nums[j],ma)
        #         ans += ma - mi
        # return ans 
        
        #Two stacks, one (I) for decreasing and one (II) for increasing, soln by lee215
        #(I) keeps track of being the lowest bound, how many times to the left and to the right
        #(II) the highest bound by the same token
        #Time O(N), space O(N)
        ans = 0
        stack = [] #(I)
        nums1 = [float('-inf')]+nums+[float('-inf')]
        for i, val in enumerate(nums1):
            while stack and nums1[stack[-1]] > val:
                j = stack.pop()
                k = stack[-1]
                ans -= nums1[j]*(i-j)*(j-k)
            stack.append(i)
            
        stack = [] #(II)
        nums2 = [float('inf')]+nums+[float('inf')]
        for i, val in enumerate(nums2):
            while stack and nums2[stack[-1]] < val:
                j = stack.pop()
                k = stack[-1]
                ans += nums2[j]*(i-j)*(j-k)
            stack.append(i)
        return ans
