# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):
​
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        ### Soln 1 - better
        l, r = 1, n
        while l < r:
            mid = l + (r - l) // 2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1;
        return l
    
        ### Soln 0 - poorly implemented binary search, slow though
        l, r = 1, n
        while l <= r:
            mid = l + (r - l) // 2
            if isBadVersion(mid) == True:
                if isBadVersion(mid-1) == False:
                    return mid
                else:
                    r = mid - 1
            else:
                if isBadVersion(mid+1) == True:
                    return mid + 1
                else: 
                    l = mid + 1
