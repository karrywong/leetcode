class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        #Brute force, time O(N^2 * len(target))
        #First attempt, time O(N * len(target)), space O(N)
        #1st sweep:construct complements in htb
        #htb = {"7":1, "777":1, "77":2} 
        #2nd sweep
        #Counter = {"777":1, "7":1, "77":2} #O(N)
#         htb = collections.defaultdict(int)
#         for num in nums:
#             if target.startswith(num):
#                 htb[target[len(num):]] += 1
        
#         counter = collections.Counter(nums)
#         ans = 0
#         for num in counter.keys():
#             if num in htb:
#                 if num * 2 == target: 
#                     ans += counter[num] * (counter[num] - 1)
#                 else:
#                     ans += htb[num] * counter[num]
#         return ans
    
        d = collections.defaultdict(int)
        for i in nums:
            d[i] += 1
       
        ans = 0
        for k, v in d.items():
            if target.startswith(k) and target[len(k):] in d:
                r = target[len(k):]
                ans += (d[k] * d[k] - d[k]) if k == r else (d[k] * d[r])
               
        return ans
        
        #nums = {"1", "1", "1", "2", "2"}, target = "12"
        #htb = {"2":3}
        #Counter = {"1":3, "2":2}
​
        #nums = {"1", "2", "2", "2"}, target = "12"
        #htb = {"2": 1}
        
        #nums = {"1"}, target "11"
        #htb = {"1": 1}
        #Counter = {"1":1}        
