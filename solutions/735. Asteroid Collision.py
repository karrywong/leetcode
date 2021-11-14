class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #[2,-1,1,-2] -> []
        #[-2,1,-1,2] -> [-2,2]
        #[5, 10, -20] -> [5, -20] -> [-20]
        #soln 1 - Leetcode greedy
        ans = []
        for asteroid in asteroids:
            while ans and asteroid < 0 < ans[-1]:
                if ans[-1] < -asteroid:
                    ans.pop()
                    continue
                elif ans[-1] == -asteroid:
                    ans.pop()
                break
            else:
                ans.append(asteroid)
        return ans
                
        # #soln 0 - first attempt
        # n = len(asteroids) #n >= 2 
        # ans = [asteroids[0]]
        # for i in range(1,n):
        #     if not ans or (ans[-1]>0 and asteroids[i]>0) or (ans[-1]<0 and asteroids[i]<0) or (ans[-1]<0 and asteroids[i]>0): 
        #         ans.append(asteroids[i])
        #         continue
        #     # ans[-1]>0 and asteroids[i]<0
        #     while ans and ans[-1] > 0 and ans[-1] < abs(asteroids[i]):
        #         ans.pop()
        #     #ans[-1] >= abs(asteroids[i])
        #     if not ans: 
        #         ans.append(asteroids[i])
        #     elif ans[-1] == abs(asteroids[i]):
