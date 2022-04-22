class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # #Counting sort - short implementation, time O(N+N)~O(N), space O(N)
        # counter = collections.Counter(heights)
        # heights_sorted = [i for i in range(1, 101) for _ in range(counter[i])]
        # return sum([1 if hs != h else 0 for hs, h in zip(heights_sorted, heights)])
        
        #Counting sort - full implementation (stable sorting), time O(N), space O(N)
        count = [0 for _ in range(101)]
        n = len(heights)
        output = [0 for _ in range(n)]
        for h in heights:
            count[h] += 1        
        for i in range(1,101):
            count[i] += count[i-1]
        ans = [0 for _ in range(n)]
        for h in heights[::-1]:
            count[h] -= 1
            ans[count[h]] = h
        return sum([1 if hs != h else 0 for hs, h in zip(ans,heights)])
