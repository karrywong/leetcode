class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # 1234 -> 1243
        # 10010 -> 10100
        # 126431 -> 131246
        #Jake's solution from Jan 2021, time O(N), space O(N)
        digits = [int(x) for x in str(n)]
        L = len(digits)
        if L == 1: return -1
        # get index of first digit from right smaller than predecessor, return -1 if none
        j = -2
        while digits[j] >= digits[j+1]:
            j -= 1
            if j == -L-1: 
                return -1
        # get index of first digit from right larger than digits[j]
        i = -1  
        while digits[j] >= digits[i]:
            i -= 1
            
        ## swap digits at i and j
        digits[i],digits[j] = digits[j],digits[i]
        # Sort the remaining digits in ascedning order
        if j < -1:
            # digits[j+1:] = sorted(digits[j+1:])
            digits[j+1:] = digits[j+1:][::-1]
        ans = sum([digits[~i]*10**i for i in range(0,L)])
        return ans if ans < 2**31 else -1
