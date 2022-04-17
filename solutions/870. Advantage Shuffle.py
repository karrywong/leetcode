class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #Time O(NlogN), space O(N), first attempt w/ sorting and counters
        n = len(nums1)
        lst = sorted(range(n), key = lambda x : nums2[x])
        ans = [0] * n
        nums1_count = collections.Counter(nums1)
        nums1.sort()
        
        j = 0
        for i in range(n):
            if nums2[lst[j]] < nums1[i]:
                ans[lst[j]] = nums1[i]
                nums1_count[nums1[i]] -= 1
                if nums1_count[nums1[i]] == 0: 
                    del nums1_count[nums1[i]]
                j += 1
        
        nums1_remains = [v for v, freq in nums1_count.items() for _ in range(freq)]
        for k in range(j, n):
            ans[lst[k]] = nums1_remains.pop()
        return ans
    
#         #LeetCode soln, similar idea, time O(NlogN), space O(N)
#         sortedB = sorted(nums2)
        
#         assigned = {b: [] for b in nums2} # assigned[b] = list of a that are assigned to beat b
#         remaining = [] # remaining = list of a that are not assigned to any b
                
#         j = 0
#         for a in sorted(nums1):
#             if a > sortedB[j]:
#                 assigned[sortedB[j]].append(a) # sortedB[j] is always the smallest unassigned element in B
#                 j += 1
#             else:
#                 remaining.append(a)
#         # Reconstruct the answer from annotations (assigned, remaining)
#         return [assigned[b].pop() if assigned[b] else remaining.pop() for b in nums2]
