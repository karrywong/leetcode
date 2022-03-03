class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        #DP approach
        #Time O(len(nums)^2 * m), space O(len(nums) * m)
        n = len(nums)
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1]+num)
        
        @lru_cache(maxsize = None)
        def get_min_largest_split_sum(cur_ind: int, subarray_count: int) -> int:
            if subarray_count == 1:
                return prefix_sum[n] - prefix_sum[cur_ind]
            
            val = prefix_sum[n] #minimum_largest_split_sum
            for i in range(cur_ind, n-subarray_count+1):
                first_split_sum = prefix_sum[i+1]-prefix_sum[cur_ind]
                largest_split_sum = max(first_split_sum, get_min_largest_split_sum(i+1, subarray_count-1))
                val = min(val, largest_split_sum)
                
                if first_split_sum > val:
                    break
            return val
        return get_min_largest_split_sum(0, m)
        
#         #Problem is to minimize the largest subarray sum
#         #Identical to problem 1231. Divide Chocolate
#         #Time O(len(nums)*log(O(sum(nums)))), space O(1)
#         def isPossible(val:int) -> bool:
#             count = 1
#             cur_sum = 0
#             for num in nums:
#                 if cur_sum + num > val:
#                     count += 1
#                     cur_sum = 0
#                 cur_sum += num
#             return count <= m
            
#         l, r  = max(nums), sum(nums)
#         while l < r:
#             mid = l + (r-l) // 2
#             if isPossible(mid):
#                 r = mid
#             else:
#                 l = mid+1
#         return l
