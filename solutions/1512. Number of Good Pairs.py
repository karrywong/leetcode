from collections import defaultdict
​
​
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # time O(N), space O(N)
        lookup = defaultdict(int)
        ans = 0
        for num in nums:
            if lookup[num] > 0:
                ans += lookup[num]
            lookup[num] += 1
        return ans
        
        # # time O(N), space O(N)
        # counter = Counter(nums)
        # ans = 0
        # for val, freq in counter.items():
        #     if freq > 1:
        #         ans += freq * (freq-1) // 2
        # return ans
                
