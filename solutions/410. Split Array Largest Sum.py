class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        #Problem is to minimize the largest subarray sum
        #Identical to problem 1231. Divide Chocolate
        #Time O(len(nums)*log(O(sum(nums)))), space O(1)
        def isPossible(val:int) -> bool:
            count = 1
            cur_sum = 0
            for num in nums:
                if cur_sum + num > val:
                    count += 1
                    cur_sum = 0
                cur_sum += num
            return count <= m
            
        l, r  = max(nums), sum(nums)
        while l < r:
            mid = l + (r-l) // 2
            if isPossible(mid):
                r = mid
            else:
                l = mid+1
        return l
