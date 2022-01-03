class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        #Leetcode one pass, time O(N), space O(N)
        remainders = collections.defaultdict(int)
        ans = 0
        for t in time:
            if t % 60 == 0: #check if a%60 == 0 && b%60 == 0
                ans += remainders[0]
            else:
                ans += remainders[60-t%60]
            remainders[t%60] += 1
        return ans
        
        #Time O(N), Space O(N)
        #mod whole list by 60, O(N)
        #counter, O(N)
        #check 0 and 30 (special case), from 1 to 29, O(N)
        
        #eg1: [30,20,30,40,40], {20: 1, 30: 2, 40:2}
        # ans = nCk(2,2) + counter[20] * counter[60-20]
        #eg2: [0,0,0], {0:3}, ans = nCk(3,2)
        
        count = collections.Counter([t%60 for t in time])
        ans = 0
        specials = [0,30]
        for s in specials:
            if s in count:
                ans += count[s]*(count[s]-1)//2
        for i in range(1,30):
            if i in count and 60-i in count:
