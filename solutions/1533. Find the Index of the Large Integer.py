# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#    # Compares the sum of arr[l..r] with the sum of arr[x..y]
#    # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#    # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#    # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#    # Returns the length of the array
#    def length(self) -> int:
#
​
class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        #Inspired by htkzmo in discussion, much cleaner code
        #Time O(logN), space O(1)
        n = reader.length()
        lo, hi = 0, n - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            compare = reader.compareSub(lo, mid, mid + 1, hi) if (hi - lo + 1) % 2 == 0 else reader.compareSub(lo, mid, mid, hi)
            if compare < 0:
                lo = mid + 1 
            else:
                hi = mid
        return lo
        
        #First attempt, screwed up - code ugly and difficult to read
        #Binary search, time O(logN), space O(1)
        l, y = 0, reader.length()-1
        if y == 1: return 0 if reader.compareSub(l,l,y,y) == 1 else 1
        while l+1 < y:
            if (y-l+1)%2 == 1: #odd length
                mid = l + ((y-l)>>1)
                r, x = mid-1, mid+1
                val = reader.compareSub(l, r, x, y) 
                if val == 1:
                    y = r 
                elif val == -1:
                    l = x
                else:
                    return mid
            else: #even length
                r = l+((y-l)>>1)
                x = r+1
                val = reader.compareSub(l, r, x, y)
                if val == 1:
                    y = r
                else:
                    l = x            
        return l if reader.compareSub(l,l,y,y) == 1 else y
