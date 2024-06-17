from collections import Counter
​
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        #nums1 = [1,3,4]
        #nums2 = [1,3,4] -> freqs ={1:1, 3:1, 4:1}
        
        # tricky
        freqs = Counter(num * k for num in nums2)
        counts = [0] * (max(nums1)+1)
​
        for num, count in freqs.items(): #O(len(nums2))
            for multiplier in range(num, len(counts), num): #O(max(nums1)/min(nums2))
                counts[multiplier] += count
        
        return sum(counts[num] for num in nums1)
        
        # time O(n*logn*sqrt(n)), m=len(nums1), n=len(nums1), space O(m*n)
        # nums1 changed in-place        
#         nums1 = [x//k for x in nums1 if x%k==0]
#         counter1 = Counter(nums1)
#         counter2 = Counter(nums2)
#         ans = 0
        
#         for x in sorted(counter1):
#             for factor in range(1, floor(sqrt(x))+1):
#                 q, r = divmod(x,factor)
#                 if r != 0: continue 
#                 if factor in counter2:
#                     ans += counter1[x] * counter2[factor]
#                 if q > factor and q in counter2:
#                     ans += counter1[x] * counter2[q]
        
        # for x in sorted(counter1):
        #     for y in sorted(counter2):
        #         if x<y: break
        #         if x%y==0:
        #             ans += counter1[x]*counter2[y]
        return ans
    
    # Testing
    # nums1 = [1,3,4], nums2 = [1,3,4], k = 1
    # nums1=[1,3,4], nums2=[1,3,4]
    # x=1, y=4
    # ans=5
    
    
