class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        #First, lights = [[-3,2],[1,2],[3,3]] -> ranges = [[-5,-1], [-1,3], [0, 6]] -> range: [-5, 6]
        #Second, loop over range, for i in [-5, 6], 
        #Third, loop over ranges,   counts = [1] -> 
        #Time O(len(range) * len(lights) )
        
        #First, ranges = [[-5,-1], [-1,3], [0, 6]] 
        #Second, starts = [-5,-1,0], ends = [-1,3,6]
        #two pointers, ans = (2, -1), count = 1
        
        starts = []
        ends = []
        for pos, val in lights:
            starts.append(pos-val)
            ends.append(pos+val)
        starts.sort()
        ends.sort()
        
        i, j = 0, 0
        count = 0
        ans = (None, 0)
        while i < len(lights):
            if starts[i] <= ends[j]:
                count += 1
                if count > ans[1]:
                    ans = (starts[i], count)
                i += 1
            else: 
                count -= 1
                j += 1
        return ans[0]        
