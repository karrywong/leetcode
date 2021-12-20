class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        #Time O(1), Space O(1), by Pager07 in discussion, make use of given constraints
        _nums1, _nums2 = [0] * 101, [0]*101
        for i in nums1:
            _nums1[i] += 1
        for i in nums2:
            _nums2[i] += 1
        p1=0 
        p2 = 100
        res  = 0 
        while p1 <= 100 and p2>=0:
            if _nums1[p1] > 0 and _nums2[p2] > 0:
                res += (p1 * p2)
                _nums1[p1] -= 1 
                _nums2[p2] -= 1
            if _nums1[p1] == 0:
                p1 += 1 
            if _nums2[p2] == 0:
                p2 -= 1
        return res     
        
        #Sorting, time O(NlogN), space O(1)
        # return sum(x*y for x,y in zip(sorted(nums1), sorted(nums2, reverse = True)))
