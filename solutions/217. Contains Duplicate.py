class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #soln 2 - set, on liner
        return len(set(nums)) < len(nums)
        
        #soln 1 - built-in counter, time O(n)
        # lib = collections.Counter(nums)
        # return not all([v == 1 for v in lib.values()])
        
        #soln 0 - set w/ many built-in fts, O(nlogn) because of sorting
        #return sorted(nums) != sorted(list(set(nums)))
        
