import random
class Solution:
    def __init__(self, w: List[int]):
        self.lst = [w[0]] #prefix sum
        for num in w[1:]:
            self.lst.append(self.lst[-1] + num) #Space O(N)
​
    def pickIndex(self) -> int:
        guess = random.randint(1,self.lst[-1]) # closed interval [1, self.lst[-1]]
        # for idx, num in enumerate(self.lst): #Time O(N)
        #     if guess <= num:  
        #         return idx
        
        # Binary search # Time O(NlogN)
        l, r = 0, len(self.lst)
        while l < r:
            mid = l + (r-l) // 2
            if guess > self.lst[mid]:
                l = mid + 1
            else:
                r = mid
        return l
        
​
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
