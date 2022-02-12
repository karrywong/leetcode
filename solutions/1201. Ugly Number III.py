class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        #Follow the given hints, answer by otoc
        #Idea is binary search using f(A) = # pos integers <= A that are divisible by a or b or c
        #Time O(1) since [1, 2*10**9] is a fixed interval
        def lcm(x, y):
            return x*y // math.gcd(x,y)
        ab, bc, ca = lcm(a, b), lcm(b, c), lcm(c, a)
        abc = lcm(ab, c)
​
        def countUgly(n): #Inclusion-exclusion principle
            answer = n//a + n//b + n//c
            answer -= n//ab + n//bc + n//ca
            answer += n//abc
            return answer
        
        l, r = 1, 2 * 10**9
        while l < r:
            mid = l + (r-l)//2
            if countUgly(mid) < n:
                l = mid + 1
            else:
                r = mid
        return l
