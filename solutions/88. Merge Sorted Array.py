class Solution:
    # follow-up m_0, .., m_(k-1)
    # List[List[int]], [[1,2,4], [2,3,5], [3,3,3,3,3], [1,4,5], ...]
    # each step, O(k)
    # time O([m_0+m_1+...+m_(k-1)]*k)
    # mergesort
    
    # Time O(m+n), space O(1)
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # # attempt 1
        # ptr1, ptr2, ptr = m-1, n-1, m+n-1
        # while ptr > -1:
        #     if ptr2==-1 or (ptr1 > -1 and nums1[ptr1] >= nums2[ptr2]):
        #         nums1[ptr] = nums1[ptr1]
        #         ptr1 -= 1
        #     elif ptr1==-1 or (ptr2 > -1 and nums1[ptr1] < nums2[ptr2]):
        #         nums1[ptr] = nums2[ptr2]
        #         ptr2 -= 1
        #     ptr -= 1
        # return 
        
        # attempt 2
        ptr1, ptr2, ptr = m-1, n-1, n+m-1
        while ptr1 >= 0 or ptr2 >= 0:
            if ptr1 == -1:
                nums1[ptr] = nums2[ptr2]
                ptr2 -= 1
            elif ptr2 == -1:
                break
            elif nums2[ptr2] <= nums1[ptr1]:
                nums1[ptr] = nums1[ptr1]
                ptr1 -= 1
            else:
                nums1[ptr] = nums2[ptr2]
                ptr2 -= 1
            ptr -= 1
​
        # #soln 2 - LeetCode backward, Time O(M+N), Space O(1)
        # p1, p2 = m-1, n-1
        # for p in range(n+m-1, -1, -1):
        #     if p2 < 0:
        #         break
        #     if p1 >= 0 and nums1[p1] > nums2[p2]:
        #         nums1[p] = nums1[p1]
        #         p1 -= 1
        #     else:
        #         nums1[p] = nums2[p2]
        #         p2 -= 1
