class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        ### Soln 0 - set intersection, time complexity O(N1 + N2 + N3)
        set1 = set(arr1)
        set2 = set(arr2)
        set3 = set(arr3)
        return sorted(list(set1 & set2 & set3))
        
