class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        # consult horwardL
        # Scan from right to left, find the largest number that is smaller than arr
        # Find A[i] where A[i] > A[i + 1] for 0 <= i < A.length - 1.
        i = len(arr)-2
        while i >= 0 and arr[i] <= arr[i+1]:
            i -= 1
        # we need to swap with the largest number that smaller than A on the right side of A[i], because we want to keep it the largest number smaller than A.
        if i >= 0:
            max_ = i+1
            for j in range(i+2, len(arr)):
                if arr[max_] < arr[j] < arr[i]:
                    max_ = j
            arr[max_], arr[i] = arr[i], arr[max_]
        return arr
        
        # [1,7,3] -> [1,3,7]
        # [3,7,1,2,3,4,5,6] -> [3,6,1,2,3,4,5,7] (-> [3,6,7,5,4,3,2,1]) not allowed
        # [1,6,3,4,8] -> [1,4,3,6,8]
        # [1,6,3,4,8,5] -> [1,6,3,4,5,8]
        # [9,1,6,3,4,8] -> [9,1,4,3,6,8]
        
        # [3,1,2] -> [2,1,3]
        # [3,1,2,2] -> [2,1,3,2]
        
        # Failed, overcomplicated
#         h = len(arr)-1 # max val index
