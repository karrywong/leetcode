class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        #Leetcode soln, adpated from 15. 3Sum
        #Time O(N^2), Space O(N)
        count = collections.Counter(arr)
        keys = sorted(count)
        
        ans = 0
        for i, x in enumerate(keys):
            T = target - x
            j, k = i, len(keys) - 1
            while j <= k:
                y, z = keys[j], keys[k]
                if y + z < T:
                    j += 1
                elif y + z > T:
                    k -= 1
                else: # x+y+z == T, now calculate the size of the contribution
                    if i < j < k:
                        ans += count[x] * count[y] * count[z]
                    elif i == j < k:
                        ans += count[x] * (count[x] - 1) // 2 * count[z]
                    elif i < j == k:
                        ans += count[x] * count[y] * (count[y] - 1) // 2
                    else:  # i == j == k
                        ans += count[x] * (count[x] - 1) * (count[x] - 2) // 6
                    j += 1
                    k -= 1     
        return ans % (10**9 + 7)
