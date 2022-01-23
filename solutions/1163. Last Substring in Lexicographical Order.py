class Solution:
    def lastSubstring(self, s: str) -> str:
        # #brute force, time O(N^2), space O(N^2)
        # arr = [s[i:] for i in range(len(s))]
        # return max(arr)
        
        #soln by hzhaoc in discussion, time O(N) since
        # O(N) to find all indices with max ASCII and then comparison of N/k substrings, O(k*N/k) = O(N)
        unique = set(s)
        if len(unique) == 1:
            return s
        
        arr, ch_max, maxl, n, prei = [-1], max(unique), 0, len(s), -1
        # find all (start i) of longest repeated substring of biggest character
        for i in range(n+1):
            if i < n and s[i] == ch_max:
                if prei < 0:
                    prei = i
            else:
                if prei >= 0:
                    l = i - prei
                    if l == maxl:
                        arr.append(prei)
                    elif l > maxl:
                        arr = [prei]
                        maxl = l
                prei = -1
        # print(arr, maxl)
        arr = [(s[si+maxl:ei] if si + maxl < n else '', -si) for si, ei in zip(arr, arr[1:] + [n])]
        # print(arr, max(arr))
        return s[-max(arr)[1]:]
    
#         #soln by henryEECS in discussion w/ straightforward idea:
#         #find character with max ASCII and compare them with each other by looking the next character. Return the solution until only one left.
#         #Smart implementation for comparsion
#         #Time O(N^2) since every character, space O(N)
#         max_ord = max([ord(c) for c in s])
#         max_ord_idxs = [i for i in range(len(s)) if ord(s[i]) == max_ord]
#         first_unique_idx = [i for i in range(len(max_ord_idxs)-1, -1, -1) if i == 0 or max_ord_idxs[i]-1 != max_ord_idxs[i-1] ]
#         max_ord_idxs = [max_ord_idxs[i] for i in first_unique_idx]
#         if len(max_ord_idxs) == 1:
#             return s[max_ord_idxs[0]:]
        
#         def findNextMaxOrd(cur_idxs, level):
#             nextOrd2CurIdx = collections.defaultdict(list)
#             hist_max = float('-inf')
#             for idx in cur_idxs:
#                 if idx < len(s) - level:
#                     nextOrd2CurIdx[ord(s[idx+level])].append(idx)
#                     hist_max = max(hist_max, ord(s[idx+level]))
#             return nextOrd2CurIdx[hist_max]
​
#         # Filtering indexes with maximum ord by comparing k-level away
#         level = 1
#         while 1:
#             max_ord_idxs = findNextMaxOrd(max_ord_idxs, level)
#             if len(max_ord_idxs) == 1:
#                 return s[max_ord_idxs[0]:]
#             level += 1
