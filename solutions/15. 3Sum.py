class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def _is_two_sum(arr: List[int], idx: int) -> None:
            target = -nums[idx]
            lookup = set()
            for num in arr[idx+1:]:
                if num in lookup:
                    ans.add(tuple(sorted([num, target-num, arr[idx]])))
                lookup.add(target - num)
            return
        
        seen = set()
        ans = set()
        for i in range(len(nums)):
            if nums[i] not in seen:
                _is_two_sum(nums, i)
                seen.add(nums[i])
        return list(ans)
​
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
#                     r -= 1
#                     while l < r and nums[l] == nums[l-1]:
#                         l += 1
        
#         ans = []
#         nums.sort()
#         for i in range(len(nums)-2):
#             if nums[i] > 0:
#                 break
#             if i == 0 or nums[i] != nums[i-1]:
#                 twoSum(i, ans)
#         return ans
