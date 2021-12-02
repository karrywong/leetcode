class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # #Jake's soln - linear scan + hashset
        # seen = collections.defaultdict(int)
        # for i in range(10, len(s)+1):
        #     seen[s[i-10:i]] += 1
        # return [x for x in seen if seen[x] > 1]
​
        #Soln 2 - bit manipulation
        L, n = 10, len(s)
        if n <= L:
            return []
        
        # convert string to the array of 2-bits integers:
        # 00_2, 01_2, 10_2 or 11_2
        to_int = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        nums = [to_int.get(s[i]) for i in range(n)]
        
        bitmask = 0
        seen, output = set(), set()
        # iterate over all sequences of length L
        for start in range(n - L + 1):
            # compute bitmask of the sequence in O(1) time
            if start != 0:
                # left shift to free the last 2 bit
                bitmask <<= 2
                # add a new 2-bits number in the last two bits
                bitmask |= nums[start + L - 1]
                # unset first two bits: 2L-bit and (2L + 1)-bit
                bitmask &= ~(3 << 2 * L)
            # compute bitmask of the first sequence in O(L) time
            else:
                for i in range(L):
                    bitmask <<= 2
                    bitmask |= nums[i]
            if bitmask in seen:
                output.add(s[start:start + L])
            seen.add(bitmask)
        return output
​
#         Soln 1 - Robin-Karp algorithm
#         L, n = 10, len(s)
#         if n <= L:
#             return []
        
#         # rolling hash parameters: base a
#         a = 4
#         aL = pow(a, L) 
        
#         # convert string to array of integers
#         to_int = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
#         nums = [to_int.get(s[i]) for i in range(n)]
        
#         h = 0
#         seen, output = set(), set()
#         # iterate over all sequences of length L
#         for start in range(n - L + 1):
#             # compute hash of the current sequence in O(1) time
#             if start != 0:
#                 h = h * a - nums[start - 1] * aL + nums[start + L - 1]
#             # compute hash of the first sequence in O(L) time
#             else:
#                 for i in range(L):
#                     h = h * a + nums[i]
#             # update output and hashset of seen sequences
#             if h in seen:       
#                 output.add(s[start:start + L])
#             seen.add(h)
#         return output
