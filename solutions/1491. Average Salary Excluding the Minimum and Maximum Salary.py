class Solution:
    def average(self, salary: List[int]) -> float:
        #Time O(N), space O(N)
        maxval, minval = float('-inf'), float('inf')
        ans = 0
        for val in salary:
            ans += val
            maxval = max(maxval, val)
            minval = min(minval, val)
        return (ans-maxval-minval)/(len(salary)-2)
