class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        #Solution by blue_sky5 in discussion, really clever
        #time O(N^2), space O(N^2)
        #observe nums[a]+nums[b] == nums[d]-nums[c], use one dictionary to record nums[c]+nums[d]
        idx = defaultdict(list)
        for i in range(len(nums)-1): #index c
            for j in range(i+1, len(nums)): #index d
                idx[nums[j]-nums[i]].append(i)
        # print(idx)
        ans = 0
        for i in range(len(nums)-1): #index a
            for j in range(i+1, len(nums)): #index b
                ans += sum([1 for k in idx[nums[i]+nums[j]] if k > j])
        return ans
        
        # #first attempt, enumerate over all possible combinations, time O(N^4), space O(1)
        # n, ans = len(nums), 0
        # for d in range(3, n):
        #     for c in range(2,d):
        #         for b in range(1,c):
        #             for a in range(b):
        #                 if nums[a] + nums[b] + nums[c] == nums[d]:
        #                     ans += 1
        # return ans
