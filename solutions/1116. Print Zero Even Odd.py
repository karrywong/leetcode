from threading import Lock
#Concurrency: Race condition. Idea is to use Lock, similar to 1114. Print in Order & 1115. Print FooBar Alternately
#Implementation by nightybear <https://leetcode.com/problems/print-zero-even-odd/discuss/359678/Python-Solution-using-Lock>
​
class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.locks = (Lock(),Lock(),Lock())
        self.locks[1].acquire() #odd
        self.locks[2].acquire() #even
        
    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n): #i from 0 to n-1
            self.locks[0].acquire()
            printNumber(0)
            if i % 2 == 0:
                self.locks[1].release()
            else:
                self.locks[2].release()
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n+1, 2):
            self.locks[2].acquire()
            printNumber(i)
            self.locks[0].release()
        self.locks[2].release()
    
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n+1, 2):
            self.locks[1].acquire()
            printNumber(i)
            self.locks[0].release()
        self.locks[1].release()
        
