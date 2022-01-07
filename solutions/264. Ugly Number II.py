class Solution:
    def nthUglyNumber(self, n: int) -> int:
        #Inspired by swastik1712 in discussion, Time O(N), Space O(N)
        dp = [1]*n
        p2 = p3 = p5 = 0
        for i in range(1,n):
            np2, np3, np5 = 2*dp[p2], 3*dp[p3], 5*dp[p5]
            # print(i, np2, np3, np5)
            uglyNumber = min(np2, np3, np5)
            dp[i] = uglyNumber
            if np2 == uglyNumber:
                p2 += 1
            if np3 == uglyNumber:
                p3 += 1
            if np5 == uglyNumber:
                p5 += 1
        return dp[-1]
    
        # #Inspired by basil123 using set, Time O(N^2), Space O(N)
        # uglyNumbers = set()
        # nextUglyNumbers = set([1])
        # factors = [2,3,5]
        # while len(uglyNumbers) < n:
        #     uglyNumber = min(nextUglyNumbers)
        #     uglyNumbers.add(uglyNumber)
        #     nextUglyNumbers.remove(uglyNumber)
        #     for num in factors:
        #         nextUglyNumbers.add(num*uglyNumber)
        # return max(uglyNumbers)
