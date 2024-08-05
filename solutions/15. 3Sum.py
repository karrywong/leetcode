class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ## soln 3 - my solution, time O(N^2), space O(N^2)
        ans, seen = set(), set()
        def _is_two_sum(nums: List[int], idx:int) -> None:
            target = -nums[idx]
            lookup = set() # target - x
            for num in nums[idx+1:]:
                if num in lookup:
                    ans.add(tuple(sorted([num, target-num, nums[idx]])))
                lookup.add(target-num)
            return
        
        for idx, num in enumerate(nums):
            if num not in seen:
                _is_two_sum(nums, idx)
                seen.add(num)
        return list(ans)
        
        # #soln 2 - Leetcode w no-sorting
        # res, dups = set(), set()
        # seen = {}
        # for i, val1 in enumerate(nums):
        #     if val1 not in dups:
        #         dups.add(val1)
        #         for j, val2 in enumerate(nums[i+1:]):
        #             complement = -val1 - val2
        #             if complement in seen and seen[complement] == i:
        #                 res.add(tuple(sorted((val1, val2, complement))))
        #             seen[val2] = i
        # return res
        
#         #soln 1 - Leetcode two pointers, Time O(n^2), Space O(n)
#         def twoSum(i, ans):
#             l, r = i+1, len(nums)-1
#             while l < r:
#                 val = nums[i] + nums[l] + nums[r]
#                 if val < 0:
#                     l += 1
#                 elif val > 0:
#                     r -= 1
#                 else:
#                     ans.append([nums[i], nums[l], nums[r]])
#                     l += 1
