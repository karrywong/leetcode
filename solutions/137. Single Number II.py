class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #soln 1- Leetcode bit manipulation, counters for seen once and twice
        #Partly Equivalent to below, b = seen_once
        #b = ~a&b&~n|~a&~b&n = ~a & (b^n)
        seen_once, seen_twice = 0,0
        for n in nums:
            seen_once = ~seen_twice & (seen_once^n)
            seen_twice = ~seen_once & (seen_twice^n)
        return seen_once
        
        # #soln 0 - digital logic design + boolean algebra
        # #ref "leetcode bit manipulation"
        # temp, a, b = 0, 0, 0
        # for n in nums:
        #     temp = a&~b&~n|~a&b&n
        #     b = ~a&b&~n|~a&~b&n #seen once
        #     a = temp
        #     # print(n,a,b, bin(a), bin(b))
        # return b
