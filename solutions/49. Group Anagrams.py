class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ### Soln 1 - LeetCode answer, smart! defaultdict is the key
        lib = collections.defaultdict(list)
        for s in strs:
            lib[tuple(sorted(s))].append(s)
        return lib.values()
        
        ### Soln 2 - even better
        # ans = collections.defaultdict(list)
        # for s in strs:
        #     count = [0] * 26
        #     for c in s:
        #         count[ord(c) - ord('a')] += 1
        #     ans[tuple(count)].append(s)
        # return ans.values()
        
#         ### Soln 0 - original attempt, O(N^2), super slow
#         lst = [sorted(tuple(s)) for s in strs]
#         ele = set([tuple(e) for e in lst])
#         res = []
        
#         i = 0
#         for a in ele:
#             res.append([])
#             alist = list(a)
#             for j, b in enumerate(lst):
#                 if alist == b: 
#                     if not res[i]: 
#                         res[i] = [strs[j]]
#                     else:
#                         res[i].append(strs[j])
