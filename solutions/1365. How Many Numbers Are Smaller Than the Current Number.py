class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        #Hashtable, time O(NlogN), space O(N)
        lookup = collections.defaultdict(list)
        for i, x in enumerate(nums):
            lookup[x].append(i)
        lst = sorted(list(set(nums)))
        ans = [0] * len(nums)
        cnt = 0
        for y in lst:
            for idy in lookup[y]:
                ans[idy] = cnt
            cnt += len(lookup[y])
        return ans
        
        # #first attempt one-liner using sort and binary search, time O(NlogN), space O(N)
        # nums_sorted = sorted(nums)
        # ans = []
        # for nums in nums:
        #     ans.append(bisect.bisect_left(nums_sorted, nums))
        # return ans
