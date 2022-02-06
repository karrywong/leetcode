class Bitset:
    #Soln by lee215 - bit manipulation, super clever
    #All operations O(1) except toString
    def __init__(self, size: int):
        self.a = 0
        self.size = size
        self.cnt = 0
​
    def fix(self, idx: int) -> None:
        val = 1 << idx
        if self.a & val == 0:
            self.a |= val
            self.cnt += 1
            
    def unfix(self, idx: int) -> None:
        val = 1 << idx
        if self.a & val:
            self.a ^= val
            self.cnt -= 1
            
    def flip(self) -> None:
        val = (1 << self.size) - 1
        self.a ^= val
        self.cnt = self.size - self.cnt
        
    def all(self) -> bool:
        return self.cnt == self.size
​
    def one(self) -> bool:
        return self.cnt > 0
​
    def count(self) -> int:
        return self.cnt
​
    def toString(self) -> str:
        ans = bin(self.a)[2:]
        return ans[::-1] + '0' * (self.size - len(ans))
​
# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()
