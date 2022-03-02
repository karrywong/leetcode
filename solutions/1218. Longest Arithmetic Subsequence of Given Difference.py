class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        #lookup = {} #key: arr[i], value: length of longest arithmetic subsequence ending in arr[i]
        #loop over arr
        #[1,2,3,4,4]
        #eg1, lookup = {1:1, 2:2, 3:3, 4:4} -> 4, maximal lookup's value
        #eg2, lookup = {1:1, 3:1, 5:1, 7:1} -> 1
        #eg3, lookup = {1:4, 5:1, 7:1,8:1,5:2,3:3, 4:1, 2:2} -> 4
        
        #Time O(N), space O(N)
        lookup = {}
        for ele in arr:
            if ele - difference in lookup:
                lookup[ele] = lookup[ele - difference] + 1
            else:
                lookup[ele] = 1
        return max(lookup.values())
