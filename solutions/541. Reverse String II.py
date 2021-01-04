class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ##Soln 1       
        chunk = [s[i: i + 2*k] for i in range(0, len(s), 2*k)]
        
        temp = ""
        for j in range(0, len(chunk)):
            if j == len(chunk) - 1 and len(chunk[j]) < k:
                temp += chunk[j][::-1]
            else:
                temp += chunk[j][k-1::-1]
                temp += chunk[j][k:]
        return temp
​
        # ###Soln 2
        # N = len(s)
        # res = ""
        # pos = 0
        # while pos < N:
        #     nx = s[pos : pos + k]
        #     res = res + nx[::-1] + s[pos + k : pos + 2 * k]
        #     pos += 2 * k
        # return res
        
        # #Soln Leetcode:
        # a = list(s)
        # for i in range(0, len(a), 2*k):
        #     a[i:i+k] = reversed(a[i:i+k])
        # return "".join(a)
    
        
