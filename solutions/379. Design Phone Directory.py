class PhoneDirectory:
​
    def __init__(self, maxNumbers: int):
        self.hp = list(range(maxNumbers))
        self.used = set()
​
    def get(self) -> int:
        if self.hp:
            num = heapq.heappop(self.hp)
            self.used.add(num)
            return num
        else:
            return -1
​
    def check(self, number: int) -> bool:
        return number not in self.used
​
    def release(self, number: int) -> None:
        if number in self.used:
            heapq.heappush(self.hp, number)
            self.used.remove(number)
​
​
# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
