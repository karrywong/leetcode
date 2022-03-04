class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        #Modified mergesort, see 912. Sort an Array
        #See yuanzhi247012's post for detailed explanation <https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/327757/Python-merge-sort-clear-explanation-and-think-process>
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            middle = len(arr) // 2
            left = merge_sort(arr[:middle])
            right = merge_sort(arr[middle:])
            merged = []
            
            j = 0
            for i in range(len(left)):
                while j < len(right) and right[j][0] < left[i][0]:
                    j += 1
                left[i][2] += j
            return sorted(left + right)
        nums_sorted = merge_sort([[v,i,0] for i, v in enumerate(nums)])
        return [cnt for _, _, cnt in sorted(nums_sorted, key = lambda x : x[1])]
        
        # #First attempt - not optimal, Time O(N^2), space O(N)
        # ans = [0]
        # lst = [nums[-1]]
        # for i in range(len(nums)-2, -1, -1):
        #     ind = bisect.bisect_left(lst, nums[i]) #logN
        #     ans.append(ind)
        #     lst.insert(ind, nums[i]) #O(N)
        # return ans[::-1]
