class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        ### Soln 2 - Stefan Pochmann using itertools
        # key = lambda s: [(ord(c) - ord(s[0])) % 26 for c in s]
        # return [list(g) for _, g in itertools.groupby(sorted(strings, key=key), key)]
        
        ### Soln 1 - Stefan Pochmann using defaultdict
        groups = collections.defaultdict(list)
        for s in strings:
            groups[tuple((ord(c) - ord(s[0])) % 26 for c in s)] += s,
        return groups.values()
        
        ### Soln 0 - shift function by Jake Reschke
        # shift = lambda s: ''.join([chr( (ord(x)-ord(s[0]))%26 + 97) for x in s])
        # groups = 0
        # lib = {}
        # out = []
        # for w in strings:
        #     shift_word = shift(w)
        #     if shift_word in lib:
        #         out[lib[shift_word]].append(w)
        #     else:
        #         lib[shift_word] = groups
        #         groups += 1
        #         out.append([w])
        # return out
            
                
                
