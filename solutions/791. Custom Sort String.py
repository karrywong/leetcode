class Solution:
    def customSortString(self, order: str, s: str) -> str:
        #step 1, s->count = {'a':2, } #O(N), N = len(s)
        #step 2, for char in order: #O(1)
        #        if char in count: ans.extend([char] * count[char])
        #        del count[char]
        
        # for key in count: #O(1)
        # ans.extend()
        
        count = collections.Counter(s)
        ans = []
        for char in order:
            if char in count:
                ans.extend([char] * count[char])
                del count[char]
        
        for key in count:
            ans.extend([key] * count[key])
        return ''.join(ans)
