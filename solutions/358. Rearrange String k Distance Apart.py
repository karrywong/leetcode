class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        #Failed attempt - problem seems intractable, similar but easier problem 767. Reorganize String
        #Soln by AntaresTsao, idea: we only worry about the most frequent characters
        #Eg, s = "aaaabbbbcccddefg"->ans= a[]a[]a[]a[]->a[bcdf]a[bcdg]a[bce]a[b]
        #check if all paddings except the last one have length larger than k-1, yes return answer, else return ''
        #Time O(N), space O(N)
        count = collections.Counter(s)
        stack = sorted(list(count.items()), key = lambda x : x[1]) # sort
    
        char, hfreq = stack.pop() #most frequent char
        ans = [[char] for _ in range(hfreq)]
        while stack and stack[-1][1] == hfreq: #letters with same highest freq
            char, _ = stack.pop()
            for i in range(hfreq):
                ans[i].append(char)
        
        res = ''.join(char*freq for char, freq in stack) #remaining characters
        for i, char in enumerate(res):
            ans[i%(len(ans)-1)].append(char)
        
        for letters in ans[:-1]:
            if len(letters) < k:
                return ""
        # print(ans)
        return ''.join(''.join(letters) for letters in ans)
