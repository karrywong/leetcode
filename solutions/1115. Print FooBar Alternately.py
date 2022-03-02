from threading import Lock
#Concurrency: Race condition. Idea is to use Lock, similar to 1114. Print in Order
class FooBar:
    def __init__(self, n):
        self.n = n
        self.locks = (Lock(),Lock())
        self.locks[0].acquire()
        
    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.locks[1].acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.locks[0].release()
                
    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.locks[0].acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.locks[1].release()
