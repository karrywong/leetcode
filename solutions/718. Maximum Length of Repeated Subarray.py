class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        #Inspired by LeetCode DP w/ idea: dp[i][j] be the longest common prefix of A[i:], B[j:]
        #If A[i] == B[j], dp[i][j] = dp[i-1][j-1]+1
        #Time O(M*N), space O(M*N)
        ans = 0
        dp = [[0]*len(nums2) for _ in range(len(nums1))]
        for i in range(len(nums1)):
            if nums1[i] == nums2[0]:
                dp[i][0] = 1
                ans = 1
        for j in range(len(nums2)):
            if nums2[j] == nums1[0]:
                dp[0][j] = 1
                ans = 1
        for i in range(1, len(nums1)):
            for j in range(1, len(nums2)):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i-1][j-1]+1
                    ans = max(ans, dp[i][j])
        return ans
        
#         #LeetCode brute force, time O(M*N*min(M,N)), space O(min(M,N)) where M = len(nums1), N = len(nums2)
#         ans = 0
#         Bstarts = collections.defaultdict(list)
#         for j, y in enumerate(nums2):
#             Bstarts[y].append(j)
​
#         for i, x in enumerate(nums1):
#             for j in Bstarts[x]:
#                 k = 0
#                 while i + k < len(nums1) and j + k < len(nums2) and nums1[i + k] == nums2[j + k]:
#                     k += 1
#                 ans = max(ans, k)
#         return ans
