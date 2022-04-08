class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # #One-liner by rock, Time O(NlogN), space O(1)
        # return sorted(arr, key=lambda x: (bin(x).count('1'), x))
        
        #Time O(NlogN), space O(N)
        #create a list of binary representation $arr_bin$
        #create a dictionary, key = count ones, value = arr[i]
        arr.sort()
        lst = [bin(a) for a in arr]
        lookup = collections.defaultdict(list)
        for x, y in zip(lst, arr):
            lookup[x.count('1')].append(y)
        ans = []
        for i in range(len(bin(arr[-1])[2:])):
            ans += lookup[i]
        return ans
