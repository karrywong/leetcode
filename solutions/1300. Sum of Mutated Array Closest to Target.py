class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        #Binary search, inspired by veryvanilla's soln, time O(Nlog(max(arr))), space O(1)
        l, r = 0, max(arr)
        while l < r:
            mid = l + (r-l+1)//2 #(l+r+1)//2
            sumval = sum([mid if a > mid else a for a in arr])
            if sumval < target:
                l = mid
            elif sumval > target:
                r = mid-1
            else:
                return mid
        sumval1 = sum([l if a > l else a for a in arr])
        sumval2 = sum([l+1 if a > l+1 else a for a in arr])
        
        if target-sumval1 <= abs(target-sumval2):
            return l
        return l+1
