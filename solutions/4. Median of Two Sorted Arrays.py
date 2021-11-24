class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #Totally stuck, solution with detailed explanation at NeetCode <https://youtu.be/q6IEA26hvXc>
        #Time complexity, O(log(M, N)) from binary search
        A, B = nums1, nums2
        m, n = len(A), len(B)
        total = m + n
        half = total // 2
        if m > n: 
            A, B = B, A
            m, n = n, m
        #m <= n 
        
        l, r = 0, m-1
        while True:
            i = l + (r-l)//2 #A
            j = (half-1)-(i+1) #B
            Aleft, Aright = A[i] if i >= 0 else float("-inf"), A[i+1] if i+1 < m else float("inf")
            Bleft, Bright = B[j] if j >= 0 else float("-inf"), B[j+1] if j+1 < n else float("inf")
            
            if Aleft <= Bright and Bleft <= Aright:
                #if total odd, return middle number, else average of two numberrs
                return min(Aright, Bright) if total%2 else 0.5*(max(Aleft, Bleft) + min(Aright, Bright))
            elif Aleft > Bright:
                r = i-1
            else: #Bleft > Aright
                l = i+1
                
        # #Cheating, time O((M+N)log(M+N))
        # nums = nums1 + nums2
        # nums.sort()
        # return nums[len(nums)//2] if len(nums) % 2 == 1 else 0.5*(nums[len(nums)//2-1]+nums[len(nums)//2])
