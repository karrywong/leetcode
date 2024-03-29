from threading import Lock
​
#Recently learned concurrent computing and concepts, i.e. race conditions, deadlocks, and resource starvation. Idea is to set critical sections to ensure partial order
class Foo:
    def __init__(self):
        self.locks = (Lock(),Lock())
        self.locks[0].acquire()
        self.locks[1].acquire()
​
    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.locks[0].release()
​
​
    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.locks[0]:
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            self.locks[1].release()
​
​
    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.locks[1]:
            # printThird() outputs "third". Do not change or remove this line.
            printThird()
