class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        #First attempt, time O(N*m*k) where N = len(arr), space O(1)
        for i in range(len(arr)-m):
            pattern = arr[i:i+m]
            if i + m*k <= len(arr) and pattern*k == arr[i:i+m*k]:
                return True
        return False
            
            
