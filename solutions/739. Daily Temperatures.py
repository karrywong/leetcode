class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ### Brute force - time exceeded
        # answer = [0] * len(T)
        # for i, t in enumerate(T[:-1]):
        #     for j, s in enumerate(T[i+1:]):
        #         if t < s: 
        #             answer[i] = j + 1
        #             break
        # return answer
        
        ### Stack + hash map
        stack = []
        answer = [0] * len(T)
        
        for i, t in enumerate(T):
            while stack and t > T[stack[-1]]:
                idx = stack.pop()
                answer[idx] = i - idx
            stack.append(i)
            
        return answer        
