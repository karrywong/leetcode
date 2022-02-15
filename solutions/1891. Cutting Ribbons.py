class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        #Thoughts        
        # eg, ribbons = (99,7,5), k = 3, output = 33
        # (99, 99, 99), k = , output = 99
        
        start_sum = sum(ribbons) 
        if start_sum < k: return 0
        if k == 1: return max(ribbons)
        #TC: O(len(ribbon) * log(sum(ribbons))), binary search on [1, start_sum]:
        i = start_sum // k  #starting point
        l, r = 1, start_sum
        while l < r:
            mid = l + (r-l)//2 
            total = sum([rib // mid for rib in ribbons])
            if total >= k:
                l = mid + 1
            else:
                r = mid #terminate if l = r   
        return l-1
​
        #TC: O(sum(ribbons) * len(ribbon)) ,
        # i = start_sum // k  #starting point
        # while i > 1: #length of k ribbons
        #     total = 0
        #     for r in ribbons:
        #         total += r // i
        #     if total >= k:
        #         return i
        #     i -= 1
        # return 0 
        
        #100 ribbons of 1000
        #BS: O(100*log((10^5)))
        #slow: O(10^5 * 100)
