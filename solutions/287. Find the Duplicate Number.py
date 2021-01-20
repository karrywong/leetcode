class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        
        for n in nums:
            if n not in seen:
                seen.add(n)
            else:
                return n
