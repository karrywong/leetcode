class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:   
        # Similar but easier than 18. 4Sum
        # key idea a+b=-(c+d)
        # Time complexity O(N^2), space O(N^2)
        ans = 0
        lookup = collections.defaultdict(int)
        for a in nums1:
            for b in nums2:
                lookup[a+b] += 1
        for c in nums3:
            for d in nums4:
                ans += lookup[-(c+d)]
        return ans
    
#         #Generalization: kSumCount
#         #Follows-up: Trade-off between memory and time complexity
#         lookup = collections.defaultdict(int)
#         def nSumCount(lists):
#             addToHash(lists,0,0)
#             return countComplements(lists, len(lists)//2, 0)
            
#         def addToHash(lists, i, val):
#             if i == len(lists)//2:
#                 lookup[val] += 1
#             else:
#                 for a in lists[i]:
#                     addToHash(lists, i+1, val+a)
        
#         def countComplements(lists, i, complement):
#             if i == len(lists):
#                 return lookup[complement]
#             count = 0
#             for a in lists[i]:
#                 count += countComplements(lists, i+1, complement-a)
#             return count
        
#         return nSumCount([nums1,nums2,nums3,nums4])
