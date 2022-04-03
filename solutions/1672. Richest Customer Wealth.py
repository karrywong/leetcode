class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = sum(accounts[0])
        for i in range(1,len(accounts)):
            ans = max(ans, sum(accounts[i]))
        return ans
        
        #One-liner
        # return max(reduce(operator.add,account) for account in accounts)
