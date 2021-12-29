class Solution:
    def findLucky(self, arr: List[int]) -> int:
        # #Counter, time O(N), space O(N)
        # counter = collections.Counter(arr)
        # ans = -1
        # for k in counter:
        #     if counter[k] == k and ans < k:
        #         ans = k 
        # return ans
        
        #Sorting, time O(NlogN), space O(1)
        #Can also use heap
        arr.sort(reverse = True)
        count = 0
        for i in range(len(arr)): 
            count += 1
            if i == len(arr)-1 or arr[i] != arr[i+1]:
                if arr[i] == count:
                    return arr[i]
                count = 0
        return -1
                
