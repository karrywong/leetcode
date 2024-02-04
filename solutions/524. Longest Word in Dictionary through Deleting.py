from collections import defaultdict
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        # s = "aepl" , dictionary = ["ale","apple","monkey","plea"]
        # ans = ""
            
       # semi brute-force, runtime O(N*M + MlogM), N = len(s), M = len(dict) 
        # space O(M)
        
        # s = "abpcplea", t = "ale", runtime O(len(s))
        def is_substring(s: str, t: str) -> bool:
            i = 0
            for char in s:
                if char == t[i]:
                    i += 1
                    if i == len(t):
                        return True
            return False
    
        candidates = [word for word in dictionary if is_substring(s,word)]
        if len(candidates) == 0: return ""
    
        lookup = defaultdict(list) #key: length of word, value: list of words
        for candidate in candidates:
            lookup[len(candidate)].append(candidate)
        k = max(lookup.keys())
        return sorted(lookup[k])[0]
​
    # s = "xaybbzcdefg", dictionary = ["xyz", "abcd", "acde", "ghijk"]
    # candidates = ["xyz", "abcd", "acde"]
    # lookup = {3: ["xyz"], 4:["abcd", "acde"]} -> k = 4
    # sorted(lookup[4]) = ["abcd", "acde"] -> "abcd"
    
    # candiates.sort() # lexigraphical order
    # candidates.sort(key=len, reverse=True) # length
    # return candiates[0] if len(candiates) > 0 else ""
    
    # example 1, candidates = ["ale","apple"] -> ["apple", "ale"]
    
    # candidates = ["aa", "apple", "abcde"] -> ["aa", "abcde", "apple"] -> ["abcde", "apple", "aa"]
    
    # candidates = ["aab", "aac", "aad"] -> ["aab", "aac", "aad"] -> ["aab", "aac", "aad"]
            
