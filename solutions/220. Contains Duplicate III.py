class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        #Reference: https://leetcode.com/problems/contains-duplicate-iii/discuss/825606/Python-3-or-Official-Solution-in-Python-3-or-2-Methods-or-Explanation
        # #solution by idontknoooo, use bucket, time O(N), space O(min(N,k))
        # if not nums or t < 0: return False
        # min_val = min(nums)
        # bucket_key = lambda x: (x-min_val) // (t+1)       # A lambda function generate buckey key given a value
        # d = collections.defaultdict(lambda: sys.maxsize)  # A bucket simulated with defaultdict
        # for i, num in enumerate(nums):
        #     key = bucket_key(num)                         # key for current number `num`
        #     for nei in [d[key-1], d[key], d[key+1]]:      # check left bucket, current bucket and right bucket
        #         if abs(nei - num) <= t: return True
        #     d[key] = num    
        #     if i >= k: d.pop(bucket_key(nums[i-k]))       # maintain a size of `k` 
        # return False
        
        #solution by idontknoooo, use SortedSet, time O(Nlog(min(N,k))), space O(min(N,k))
        from sortedcontainers import SortedSet
        # Create SortedSet. `n` is the size of sortedset, max value of `n` is `k` from input
        ss, n = SortedSet(), 0                 
        for i, num in enumerate(nums):
            # index whose value is greater than or equal to `num`
            ceiling_idx = ss.bisect_left(num)  
            # index whose value is smaller than `num`
            floor_idx = ceiling_idx - 1        
            if ceiling_idx < n and abs(ss[ceiling_idx]-num) <= t: # check right neighbour  
                return True  
            if 0 <= floor_idx and abs(ss[floor_idx]-num) <= t: # check left neighbour
                return True
            ss.add(num)
            n += 1
            if i - k >= 0:  # maintain the size of sortedset by finding & removing the earliest number in sortedset
                ss.remove(nums[i-k])
                n -= 1
        return False
    
        # #Right idea but time O(N^2), TLE
        # htb = {}
        # for i, num in enumerate(nums):
        #     for val in htb:
        #         if abs(val-num) <= t and i-htb[val] <= k:
        #             return True
        #     htb[num] = i
        # return False
