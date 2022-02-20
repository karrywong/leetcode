class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        #Optimized after two attempts, time O(N), space O(1)
        i, j = 0,0
        ans = []
        while i < len(encoded1) and j < len(encoded2):
            freq = min(encoded1[i][1], encoded2[j][1])
            encoded1[i][1] -= freq
            encoded2[j][1] -= freq
            val = encoded1[i][0]*encoded2[j][0]
            
            if ans and ans[-1][0] == val:
                ans[-1][1] += freq
            else:
                ans.append([val, freq])
            
            if encoded1[i][1] == 0: 
                i += 1
            if encoded2[j][1] == 0: 
                j += 1
        return ans
