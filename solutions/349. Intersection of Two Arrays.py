class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ### Soln 0 - Set, O(N + M)
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1.intersection(set2)) 
        
        # if len(set1) <= len(set2):
        #     return [x for x in set1 if x in set2]
        # else:
        #     return [x for x in set2 if x in set1]
