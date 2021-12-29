class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # eg1 array = gas - cost = [-1,-1,-1,3,3] 
        # eg2 array = [-1,-1,1] 
        # eg3 [-1,1,-3,1,1,3]
        
        # Time O(N), space O(1)
        n = len(gas)
        curr_tank, total_tank = 0, 0
        ans = 0
        for i in range(n):
            net_gas = gas[i] - cost[i]
            curr_tank += net_gas
            total_tank += net_gas
            if curr_tank < 0:
                curr_tank = 0
                ans = i+1
        # if ans == n: ans = 0
        return ans if total_tank >= 0 else -1
        
        # #Mock interview failed, time O(N^2), space O(N)
        # arr = []
        # for g, c in zip(gas, cost):
        #     arr.append(g-c)
        # n = len(arr)
        # for i, a in enumerate(arr):
        #     if a < 0: continue
        #     j = i+1
        #     while j < i+n:
        #         a += arr[j%n] 
        #         if a < 0: break
        #         j += 1
        #     if j == i+n and a >= 0: return i
