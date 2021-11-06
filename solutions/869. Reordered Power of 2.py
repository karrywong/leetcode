class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        #soln 2 - Leetcode, exhaustion
        count = collections.Counter(str(n))
        #math.log2(10**9) ~ 29.9
        return any(count == collections.Counter(str(1<<b)) for b in range(31))
        
        
        # # #soln 1 - Leetcode one-liner
        # return any(cand[0] != '0' and bin(int("".join(cand))).count('1') == 1 for cand in itertools.permutations(str(n)))
        
        # #soln 0 - naive attempt
        # lst_digits = list(map(int, str(n)))
        # zeros = lst_digits.count(0)
        # #Generate all permutations
        # def helper(nums):
        #     if len(nums) == 1:
        #         return [nums]
        #     curr = helper(nums[1:])
        #     return [x[:i] + [nums[0]] + x[i:] for x in curr for i in range(len(nums))]
        # #exclude leading zeros
        # perm_digits = [int(''.join(map(str, lst))) for lst in helper(lst_digits) if lst[0] != 0]
        # return any(list(map(lambda x: not x&(x-1), perm_digits)))
        
        
        
