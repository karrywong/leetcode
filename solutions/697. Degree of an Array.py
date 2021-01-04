class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        freq = max(counts.values())
        if freq == 1: return 1
        
        elements = [k for k, v in counts.items() if v == freq]
        if len(elements) == 1:
            e = elements[0]
            last_index = len(nums) - nums[::-1].index(e) - 1
            return last_index - nums.index(e) + 1
        else: 
            answer = len(nums)
            for e in elements:
                last_index = len(nums) - nums[::-1].index(e) - 1
                temp = last_index - nums.index(e) + 1
                answer = min(temp, answer)
            return answer
    
    
​
