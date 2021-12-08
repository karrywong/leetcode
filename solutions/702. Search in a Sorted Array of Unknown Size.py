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
        #Time O(logN + logN) = O(logN), Space O(1) 
        #Bit manipulation to find the boundary
        if reader.get(0) == target: return 0
        l, r = 0, 1
        while reader.get(r) < target: #python doesn't have overflow issue
            l = r
            r <<= 1
        # reader.get(r) >= target
        while l <= r: #BS
            mid = l + ((r-l)>>1)
            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1
