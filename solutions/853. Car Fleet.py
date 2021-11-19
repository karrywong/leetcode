class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #discussion by lee215
        time = [(target - p) / s for p, s in sorted(zip(position, speed))]
        res = cur = 0
        for t in time[::-1]:
            if t > cur:
                res += 1
                cur = t
        return res
        
        # #first attempt, by Jake Reschke
        # state = list(zip(position,speed))
        # state.sort()
        # i = len(position) - 1
        # ans = 0
        # while i >= 0:
        #     ans += 1
        #     (cur,v) = state[i]
        #     t = (target - cur)/v
        #     j = i - 1
        #     while j >= 0 and (target - state[j][0])/state[j][1] <= t:
        #         j -= 1
        #     i = j
        # return ans
