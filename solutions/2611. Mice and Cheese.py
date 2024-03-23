# from heapq import heapify, nlargest
​
class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        # # heap, time complexity O(nlogk), space O(n)
        # k_largest_diff = nlargest(k, [r1-r2 for r1, r2 in zip(reward1, reward2)]) 
        # return sum(reward2) + sum(k_largest_diff)
        
        # See hint 2, one-liner
        # time complexity O(nlogn), space O(n)
        diff = sorted([r1-r2 for r1, r2 in zip(reward1, reward2)], reverse = True)
        return sum(reward2) + sum(diff[:k])
​
        # reward1 = [2,5]
        # reward2 = [3,8]
        # diff = [-1,-3], ans=11, k=1
        # ans = 10
        
        # reward1 = [-,-,3,4]
        # reward2 = [4,4,1,-]
        # k = 2
        # (0,0)
        
        # reward1 = [9,9,0]
        # reward2 = [10,0,8]
        # k = 1
        
        # reward1 = [3,4,4]
        # reward2 = [0,3,3]
        # diff = [3,1,1], k = 2, ans = 6
        # ans = 6+3+1 = 10
​
