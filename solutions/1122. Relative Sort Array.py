class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:        
        #Counting sort - first implementation, time O(NlogN), space O(N)
        counter = collections.Counter(arr1)
        ans = []
        for a in arr2:
            ans.extend([a]*counter[a])
            del counter[a]
        for k in sorted(counter):
            ans.extend([k]*counter[k])
        return ans
