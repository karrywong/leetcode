class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #[2,-1,1,-2] -> []
        #[-2,1,-1,2] -> [-2,2]
        #[1,1] and [-1,-1], nothing happens
        #[5, 10, -20] -> [5, -20] -> [-20]
        #[-2,-2,1,-2] -> [-2, -2, 
        #output array can be empty. If not, must be sorted
        #[1,-1,-2,-2] -> []
        
        #soln 0 - first attempt
        n = len(asteroids) #n >= 2 
        ans = []
        for i in range(n):
            if not ans or (ans[-1]>0 and asteroids[i]>0) or (ans[-1]<0 and asteroids[i]<0) or (ans[-1]<0 and asteroids[i]>0): 
                ans.append(asteroids[i])
                continue
            
            # ans[-1]>0 and asteroids[i]<0
            while ans and ans[-1] > 0 and ans[-1] < abs(asteroids[i]):
                ans.pop()
            #ans[-1] >= abs(asteroids[i])
            if not ans: 
                ans.append(asteroids[i])
            elif ans[-1] == abs(asteroids[i]):
                ans.pop()
            elif ans[-1] < 0:
                ans.append(asteroids[i])
            
        return ans
