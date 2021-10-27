class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # soln 1 - built-in function collections.Counter, Time O(max(M,N)), Space O(min(M, N))
        lib = collections.Counter(nums1) & collections.Counter(nums2)
        return [k for k in lib for i in range(lib[k])]
​
#         # soln 0 - first attempt, Time O(max(M,N) * log(max(M,N))), Space O(min(M, N))
#         nums1.sort()
#         nums2.sort()
#         n, m = len(nums1), len(nums2)
#         if m < n:
#             nums2, nums1 = nums1, nums2
#             m, n = n, m
            
#         ans = []
#         i, j = 0, 0
        
#         while i < n and j < m:
#             if nums1[i] == nums2[j]:
#                 ans.append(nums1[i])
#                 i += 1
#                 j += 1
#             elif nums1[i] > nums2[j]:
#                 j += 1
#             else:
#                 i += 1
#         return ans
