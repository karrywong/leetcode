class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # time O(n+m), space O(n+m)
        ans = [0, 0]
        set1, set2 = set(nums1), set(nums2)
        for num in nums1: #O(n)
            if num in set2:
                ans[0] += 1
        
        for num in nums2: #O(m)
            if num in set1:
                ans[1] += 1
        return ans
    
    # Testing 
    # set1 = {4,3,2,1}
    # set2 = {2,3,5,6}
    # ans[0] = 3
    # ans[1] = 4 -> [3,4]
    
    # set1 = {3,4,2}
    # set2 = {1,5}
    # ans = [0,0]
        
