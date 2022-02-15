class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        #Time O(N + QlogN), space O(N)
        indices = {k:[] for k in (1,2,3)}
        for i, color in enumerate(colors):
            indices[color].append(i)
            
        ans = []
        for i, c in queries:
            if not indices[c]:
                ans.append(-1)
            elif i <= indices[c][0]:
                ans.append(indices[c][0] - i)
            elif i >= indices[c][-1]:
                ans.append(i - indices[c][-1])
            else:
                l, r = 0, len(indices[c])-1
                bo = True
                while bo and l < r:
                    mid = l + (r-l)//2
                    if indices[c][mid] < i:
                        l = mid + 1
                    elif indices[c][mid] > i:
                        r = mid
                    else:
                        ans.append(0)
                        bo = False
                # print(l,r,indices[c],i)
                if bo: ans.append(min(i-indices[c][l-1], indices[c][l]-i))
        return ans
