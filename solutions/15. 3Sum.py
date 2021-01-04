class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dups = set()
        seen = {}
        answer = set()
        
        for i, n in enumerate(nums):
            if n not in dups:
                dups.add(n)
                for j,m in enumerate(nums[i+1:]):
                    complement = -n - m
                    if complement in seen and seen[complement] == i:
                        answer.add(tuple(sorted((n,m,complement))))
                    seen[m] = i
​
        return answer
        
