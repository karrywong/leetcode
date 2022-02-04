class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        #Failed attempt, then inspired by LeetCode DP idea
        #Time O(NlogN), space O(N)
        counts = collections.Counter(nums)
        prev = -1
        avoid, using = 0,0
        for k in sorted(counts):
            avoid_prev = avoid
            if k-1 != prev:
                avoid = max(avoid, using)
                using = max(avoid_prev, using) + counts[k]*k
            else:
                avoid = max(avoid, using)
                using = avoid_prev + counts[k]*k
            prev = k
        return max(avoid,using)
