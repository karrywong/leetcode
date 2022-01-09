class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Mock interview practice
        #stack = [(73,0)]
        #i = 1, ans[0] = 1-0, stack.pop(), stack = [(74,1)]
        #i = 2, ans[1] = 2-1, stack.pop(), stack = [(75,2)]
        #i = 3, stack.append((71,3)), stack = [(75,2),(71,3),]
        #i = 4, stack = [(75,2),(71,3),(69,4)]
        #i = 5, ans[4]=5-4=1, ans[3]=5-3=2, stack = [(75,2),(72,5)]
        
        #[90,60,30], ans = [0,0,0]
        #[3,2,1,6]
        
        #Time O(N), Space O(N)
        minTemperature = []
        ans = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while minTemperature and temperatures[i] > temperatures[minTemperature[-1]]:
                ind = minTemperature.pop()
                ans[ind] = i - ind
            minTemperature.append(i)
        return ans
    
        #Space further optimized, Time O(N), Space (1)
        hottest = 0
        n = len(temperatures)
        ans = [0]*n
        for i in range(n-1,-1,-1):
            cur_temp = temperatures[i]
            if cur_temp >= hottest:
                hottest = cur_temp
                continue
            
            days = 1
            while cur_temp >= temperature[i+ans[i+days]]:
                days += ans[i+days]
            ans[i] = days
        return ans
