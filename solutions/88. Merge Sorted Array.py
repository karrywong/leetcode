class Solution:
    # m_0, .., m_(k-1)
    # List[List[int]], [[1,2,4], [2,3,5], [3,3,3,3,3], [1,4,5], ...]
    # each step, O(k)
    # time O([m_0+m_1+...+m_(k-1)]*k)
    # mergesort
    
    # Time O(m+n), space O(1)
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """     
        ptr1, ptr2, ptr = m-1, n-1, n+m-1
        while ptr1 >= 0 or ptr2 >= 0:
            if ptr1 == -1:
                nums1[ptr] = nums2[ptr2]
                ptr2 -= 1
            elif ptr2 == -1:
                nums1[ptr] = nums1[ptr1]
                ptr1 -= 1
            elif nums2[ptr2] <= nums1[ptr1]:
                nums1[ptr] = nums1[ptr1]
                ptr1 -= 1
            else:
                nums1[ptr] = nums2[ptr2]
                ptr2 -= 1
            ptr -= 1
    
#         ptr1, ptr2 = 0, 0
#         ans = []
#         while ptr1 < m or ptr2 < n:
#             if ptr1 == m:
#                 ans.append(nums2[ptr2])
#                 ptr2 += 1
#             elif ptr2 == n:
#                 ans.append(nums1[ptr1])
#                 ptr1 += 1
#             elif nums1[ptr1] <= nums2[ptr2]:
#                 ans.append(nums1[ptr1])
#                 ptr1 += 1
#             else: 
#                 ans.append(nums2[ptr2])
#                 ptr2 += 1
        
