class RandomizedSet:
    #Time O(1), Space O(N)
    def __init__(self):
        self.lst = []
        self.htb = {} #htb, input: value, output: value's index in lst
        self.count = 0
        
    def insert(self, val: int) -> bool:
        if val in self.htb: #O(1)
            return False
        else:
            self.lst.append(val) #O(1)
            self.htb[val] = self.count
            self.count += 1
            return True
        
    def remove(self, val: int) -> bool:
        if val in self.htb: #O(1)
            if self.lst[-1] == val:
                self.lst.pop()
                del self.htb[val]
            else:
                ind = self.htb[val]
                temp = self.lst.pop() 
                self.lst[ind] = temp
                del self.htb[val] #O(1)
                self.htb[temp] = ind   
            self.count -= 1
            return True
        else:
            return False
​
    def getRandom(self) -> int:
        ind = random.randint(1, self.count) - 1 #O(1)
        return self.lst[ind]
​
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
