class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        #Mock FB interview w/ Haotian, prefix sum
        htb = collections.defaultdict(int) #key = culmative sum % k, from 0 to k-1
        cur_sum = 0
        ans = 0
        
        #time complexity: O(N), space: O(min(N,k))
        for num in nums:
            cur_sum += num
            if cur_sum % k == 0:
                ans += 1
            ans += htb[cur_sum % k]
            htb[cur_sum % k] += 1
            
        return ans 
