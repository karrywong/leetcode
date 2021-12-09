class Solution:
    def minSwaps(self, data: List[int]) -> int:
        #First attempt, after hints 1, 2 & 3, time: O(N), space O(1)
        ones = sum(data)
        val = sum(data[0:ones]) #sliding window
        i = 0
        ans = ones - val
        while i+ones < len(data):
            val -= data[i]
            val += data[i+ones]
            ans = min(ans, ones-val)
            i += 1
        return ans
