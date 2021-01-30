class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        ### Soln 2 - oneliner using Fermat's theorem
        return pow(a % 1337, (int(''.join(map(str, b)))) % 570, 1337)
        
        ### Soln 1 - recursion by cavex in discussion
        if not b:
            return 1
        return pow(a, b.pop(), 1337)* self.superPow(pow(a, 10, 1337), b) %1337
        
        ### Soln 0 - naive approach
        if a == 0 or a == 1: return a
        c = 1337
        if a >= c:
            a %= c
  
        n = 0
        b.reverse()
        for i, e in enumerate(b):
            n += e* 10**i
        return pow(a,n,1337)
