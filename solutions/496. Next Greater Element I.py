class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
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
        
        #Stefan Pochmann's one-liner
        return [next((y for y in nums2[nums2.index(x):] if y > x), -1) for x in nums1]
