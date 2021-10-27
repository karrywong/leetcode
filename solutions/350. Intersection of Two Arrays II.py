class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # soln 0 - first attempt, Time O(max(M,N) * log(max(M,N)))
        nums1.sort()
        nums2.sort()
        n, m = len(nums1), len(nums2)
        if m < n:
            nums2, nums1 = nums1, nums2
            m, n = n, m
            
        ans = []
        i, j = 0, 0
        
        while i < n and j < m:
            if nums1[i] == nums2[j]:
                ans.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return ans
            
                
        
        
