class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        #Leetcode solution using HashSet, time O(N*L), space O(L)
        #where L = 1 + log(M) w/ M = max(nums)
        # length of max number in a binary representation
        L = len(bin(max(nums))) - 2
        max_xor = 0
        for i in range(L)[::-1]:
            # go to the next bit by the left shift
            max_xor <<= 1
            # set 1 in the smallest bit
            curr_xor = max_xor | 1
            # print(i, curr_xor)
            # compute all existing prefixes 
            # of length (L - i) in binary representation
            prefixes = {num >> i for num in nums}
            # print(prefixes)
            # Update max_xor, if two of these prefixes could result in curr_xor.
            # Check if p1^p2 == curr_xor, i.e. p1 == curr_xor^p2
            # print(max_xor)
            max_xor |= any(curr_xor^p in prefixes for p in prefixes)
            # print(max_xor, [curr_xor^p in prefixes for p in prefixes])
        return max_xor        
