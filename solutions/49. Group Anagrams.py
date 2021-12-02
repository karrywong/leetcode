class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #  ### Soln 1 - LeetCode answer, smart! defaultdict is the key
        # lib = collections.defaultdict(list)
        # for s in strs:
        #     lib[tuple(sorted(s))].append(s)
        # return lib.values()
        
        ## Soln 2 - even better using key code
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()
        
        # #soln 0 - first attemp, super slow, Time O(N^2)
        # n = len(strs)
        # ans = [[strs[0]]]
        # lst_lib = [collections.Counter(strs[0])]
        # for i in range(1, n):
        #     bo = True
        #     word = strs[i]
        #     lib = collections.Counter(word)
        #     for j, lib0 in enumerate(lst_lib):
        #         if lib == lib0:
        #             ans[j].append(word)
        #             bo = False
        #             break
        #     if bo:
        #         ans.append([word])
        #         lst_lib.append(lib)
        # return ans
