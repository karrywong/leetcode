class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        #soln 2 - Leetcode one hash map
        lib, words = {}, s.split()
        if len(words) != len(pattern): 
            return False
        for i in range(len(words)):
            c, w = pattern[i], words[i]
            char_key, char_word = 'char_'+c,'word_'+w
            if char_key not in lib:
                lib[char_key] = i
            if char_word not in lib:
                lib[char_word] = i
            if lib[char_key] != lib[char_word]:
                return False
        return True
        
#         #soln 1 - Leetcode two hash maps
#         map_char, map_word = {}, {}
#         words = s.split()
#         if len(words) != len(pattern):
#             return False
        
#         for c,w in zip(pattern, words):
#             if c not in map_char:
#                 if w not in map_word:
#                     map_char[c] = w
#                     map_word[w] = c
#                 else:
#                     return False
#             else:
#                 if map_char[c] != w:
#                     return False
#         return True
        
        # #First attempt, not the fastest
        # s, lib = s.split(), {}
        # if len(pattern) != len(s): return
        # for p, w in zip(pattern, s):
        #     print(p,w)
        #     if p not in lib:
        #         lib[p] = w
        #     if lib[p] != w or sorted(list(lib.values())) != sorted(list(set(lib.values()))):
        #         return False
        # return True
