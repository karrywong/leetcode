from collections import defaultdict
from typing import List, Tuple
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # Runtime O(N * M) with N = len(nums) and M = max(len(num)), space O(N)
        # 1. build dictionary O(N), key = sum of digits, value = List[num]
        # 2. loop over dictionary, len(dict[s]) = 2 -> find two largest numbers O(N)
        # compute sum 
​
        lookup = defaultdict(list)
        for num in nums:
            digit_sum = sum([int(s) for s in str(num)])
            lookup[digit_sum].append(num)
        
        def _get_max(vec: List[int]) -> Tuple[int,int]:
            # res1, res2 = 0, 0
            # for v in vec:
            #     if v > res1:
            #         res2 = res1
            #         res1 = v
            #     elif v > res2:
            #         res2 = v
            # return res1, res2
            return heapq.nlargest(2, vec)
        
        ans = -1
        for k, lst in lookup.items():
            if len(lst) < 2:
                continue
            max_fir, max_sec = _get_max(lst)
            ans = max(ans, max_fir + max_sec)
        return ans
