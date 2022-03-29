class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # #Time O(1), space O(1)
        # if low % 2 == 1 or high % 2 == 1:
        #     return (high - low) // 2 + 1
        # else: 
        #     return (high - low) // 2
        #One-liner by lee215, #odd no in [1,low - 1] is low//2, and [1, high] is (high+1)//2
        return (high+1)//2 - low//2
