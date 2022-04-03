class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #Leetcode's stack, time O(N), space O(N)
        stack, lookup = [], {}
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                lookup[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        
        while stack:
            lookup[stack.pop()] = -1
        
        return [lookup[num] for num in nums1]
        
        # #First attempt, time O(N), space O(N), where N = len(nums2)
        # m, n = len(nums1), len(nums2)
        # ans = [-1]*m
        # htb = collections.defaultdict(lambda:-1)
        # for ind, num in enumerate(nums1):
        #     htb[num] = ind
        # stack = [] #Monotonic stack
        # for num in nums2:
        #     while stack and num > stack[-1]:
        #         ind = htb[stack.pop()]
        #         if ind > -1:
        #             ans[ind] = num
        #     stack.append(num)
        # return ans    
        
        # #Stefan Pochmann's one-liner
        # return [next((y for y in nums2[nums2.index(x):] if y > x), -1) for x in nums1]
