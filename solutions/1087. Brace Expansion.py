class Solution:
    def expand(self, s: str) -> List[str]:
        #First attempt, time O(NlogN), space O(?)
        lst = []
        i = 0
        while i < len(s):
            if s[i] == "{":
                temp = []
                i += 2
                while s[i] != "}":
                    temp.append(s[i-1])
                    i += 2
                temp.append(s[i-1])
                lst.append(tuple(sorted(temp)))
            else:
                lst.append(s[i])
            i += 1
        return [''.join(x) for x in itertools.product(*lst)]
