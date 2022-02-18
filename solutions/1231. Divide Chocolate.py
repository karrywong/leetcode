class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        #Problem is to maximize the smallest subarray sum
        #Almost identical to problems 1011. Capacity To Ship Packages Within D Days
        #and 1891. Cutting Ribbons
        #Time O(len(sweetness)* O(log(sum(sweetness)//(k+1)))), space O(1)
        def isPossible(val:int) -> bool:
            count = 0
            cur_sum = 0
            i = 0
            for sweet in sweetness:
                cur_sum += sweet
                if cur_sum >= val:
                    count += 1
                    cur_sum = 0
            return count > k
                
        l, r = min(sweetness), sum(sweetness) // (k+1) + 1
        while l < r:
            mid = l + (r-l)//2
            if isPossible(mid):
                l = mid + 1
            else:
                r = mid
        return l - 1
