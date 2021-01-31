class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:        
        # Soln 0 - my attempt
        n = len(nums)
        odd = [-1] +  [i for i in range(n) if nums[i] % 2 == 1] + [n]
        if len(odd[1:-1]) < k: return 0
        return sum([(odd[i] - odd[i-1]) * (odd[i+k] - odd[i+k-1]) for i in range(1,len(odd) - k)])
​
        # Soln 1 - DP by Jake Reschke
        # nums[0] %= 2
        # for i in range(1,len(nums)):
        #     nums[i] = nums[i] % 2 + nums[i-1]
        # print(nums)
        # count = collections.Counter(nums)
        # print(count, count[k], [count[x-k] for x in nums])
        # total = count[k] + sum([count[x-k] for x in nums])
        # return total
    
#ex1 odd = [0,1,3,4], k = 3
# i=0, j=2 -> res += (0 + 1) * (4 - 3) = 1
# i=1, j=3 -> res += (1 - 0) * (5 - 4) = 1
​
#ex2 odd = [], k = 1
# return 0
​
#ex3, odd = [3,6], k = 2
# return (3+1)*(10 - 6) = 16
​
