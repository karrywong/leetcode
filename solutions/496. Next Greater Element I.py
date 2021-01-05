class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #Soln 1 - brute force
#         library = {k: v for v, k in enumerate(nums2)} 
#         print(library)
        
#         answer = [-1]*len(nums1)
#         for i, n in enumerate(nums1):
#             for m in nums2[library[n]+1:]:
#                 if m > n: 
#                     answer[i] = m
#                     break
#         return answer
​
        #Soln 2 Stack
        if len(nums2) == 0: return []
        stack = [nums2[0]]
        library = {}
        answer = []
        
        for n in nums2[1:]:
            while stack and n > stack[-1]:
                library[stack[-1]] = n
                stack.pop()
            stack.append(n)
​
        while stack:
            library[stack.pop()] = -1
        for m in nums1:
            answer.append(library[m])
        return answer
        
