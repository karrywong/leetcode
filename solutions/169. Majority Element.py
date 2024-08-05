class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Boyer-Moore Voting Algorithm, Time O(N), Space O(1)
        answer, count = None, 0
        for n in nums:
            if count == 0:
                answer = n
            count += 1 if n == answer else -1
        return answer
        
        # #Recent attempt - hashtable, Time O(N), Space O(N)
        # n = len(nums)//2
        # counter = collections.Counter(nums)
        # for num, freq in counter.items():
        #     if freq > n:
        #         return num
        
        # #old attempt - use count(), Time O(k*N), Space O(k)
        # #where k is the number of unique elements
        # elements, count = set(nums), 0
        # for element in elements:
        #     temp = nums.count(element)
        #     if temp > count:
        #         answer, count = element, temp
        # return answer
                
        
