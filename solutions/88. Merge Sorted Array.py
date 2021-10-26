class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #soln 2 - LeetCode backward, Time O(log(M+N)), Space O(1)
        p1, p2 = m-1, n-1
        for p in range(n+m-1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
        
        # # soln 1 - Time O(log(M+N)), Space O(1), my second attempt
        # if n == 0: return nums1
        # i, j = 0, 0
        # while j < n and i < m+n:
        #     if nums1[i] > nums2[j]:
        #         for k in range(len(nums1)-1,i-1,-1):
        #             nums1[k] = nums1[k-1]
        #         nums1[i] = nums2[j]
        #         j += 1
        #     i += 1 
        # if j != n: nums1[j-n:] = nums2[j:]
        
        # # soln 0 - Time O(log(M+N)), Space O(N), my first attempt
        # if n == 0: return nums1
        # nums1[-n:] = nums2[:]
        # nums1.sort()
            
