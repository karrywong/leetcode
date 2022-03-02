from threading import Lock
​
#Recently learned concurrent computing and concepts, i.e. race conditions, deadlocks, and resource starvation. Idea is to set critical sections to ensure partial order
class Foo:
    def __init__(self):
        self.firstJobDone = Lock()
        self.secondJobDone = Lock()
        self.firstJobDone.acquire()
        self.secondJobDone.acquire()
​
    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.firstJobDone.release()
​
​
    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.firstJobDone:
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
        self.secondJobDone.release()
​
​
    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.secondJobDone:
            # printThird() outputs "third". Do not change or remove this line.
            printThird()
