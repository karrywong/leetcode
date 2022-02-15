class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #time O(len(weights)* O(log(sum(weights)))), space O(1)
        def get_days(capacity: int) -> int:
            i = 0
            cur_weight = 0
            count = 0
            while i < len(weights):
                cur_weight += weights[i]
                if cur_weight > capacity:
                    count += 1
                    cur_weight = weights[i]
                i += 1
            return count+1
        
        l, r = max(weights), sum(weights)
        while l < r:
            mid = l + (r-l)//2
            if get_days(mid) > days:
                l = mid + 1
            else: 
                r = mid
        return l
