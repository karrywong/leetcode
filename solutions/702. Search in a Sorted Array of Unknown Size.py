# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:
​
class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        ### Soln 0 - find right boundary
        r = 10000
        l = 0
        while (l <= r):
            mid = l + (r-l) // 2
            val = reader.get(mid)
            if val == target:
                return mid
            elif val < target:
                l = mid + 1
            else: 
                r = mid - 1
        
        return -1
​
#         ### Soln 1 - LeetCode solution
#         if reader.get(0) == target:
#             return 0
        
#         # search boundaries
#         left, right = 0, 1
#         while reader.get(right) < target:
#             left = right
#             right <<= 1
        
#         # binary search
