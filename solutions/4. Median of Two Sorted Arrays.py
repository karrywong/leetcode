                if i == m: #update
                    j += 1
                elif j == n:
                    i += 1
                else:
                    if A[i] <= B[j]:
                        i += 1
                    else:
                        j += 1
        
        if not nums1:
            return nums2[len(nums2)//2] if len(nums2) % 2 else 0.5*(nums2[len(nums2)//2-1] + nums2[len(nums2)//2])
        if not nums2:
            return nums1[len(nums1)//2] if len(nums1) % 2 else 0.5*(nums1[len(nums1)//2-1] + nums1[len(nums1)//2])
                                                                    
        totallen = len(nums1) + len(nums2)
        if totallen % 2:
            return helper(nums1, nums2)
        else:
            val1 = helper(nums1, nums2[:-1]) if nums1[-1] <= nums2[-1] else helper(nums1[:-1], nums2)
            val2 = helper(nums1[1:], nums2) if nums1[0] <= nums2[0] else helper(nums1, nums2[1:])
            return 0.5*(val1+val2)
        
#         #Totally stuck, solution with detailed explanation at NeetCode <https://youtu.be/q6IEA26hvXc>
#         #Time complexity, O(log(M+N)) from binary search
#         A, B = nums1, nums2
#         m, n = len(A), len(B)
#         total = m + n
#         half = total // 2
#         if m > n: 
#             A, B = B, A
#             m, n = n, m
#         #m <= n 
        
#         l, r = 0, m-1
#         while True:
#             i = l + (r-l)//2 #A
#             j = (half-1)-(i+1) #B
#             Aleft, Aright = A[i] if i >= 0 else float("-inf"), A[i+1] if i+1 < m else float("inf")
#             Bleft, Bright = B[j] if j >= 0 else float("-inf"), B[j+1] if j+1 < n else float("inf")
            
#             if Aleft <= Bright and Bleft <= Aright:
#                 #if total odd, return middle number, else average of two numberrs
#                 return min(Aright, Bright) if total%2 else 0.5*(max(Aleft, Bleft) + min(Aright, Bright))
#             elif Aleft > Bright:
#                 r = i-1
#             else: #Bleft > Aright
#                 l = i+1
                
        # #Cheating, time O((M+N)log(M+N))
        # nums = nums1 + nums2
        # nums.sort()
        # return nums[len(nums)//2] if len(nums) % 2 == 1 else 0.5*(nums[len(nums)//2-1]+nums[len(nums)//2])
