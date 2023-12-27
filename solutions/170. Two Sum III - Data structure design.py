class TwoSum:
    def __init__(self):
        self.seen = {}
        
    def add(self, number: int) -> None:
        if number not in self.seen:
            self.seen[number] = 1
        else:
            self.seen[number] += 1
    
    def find(self, value: int) -> bool:
        seen = self.seen
        for num in seen:
            if value - num in seen and (value - num != num or seen[num] > 1):
                return True
        return False
    
# # dummy soln, space O(N^2), time O(1)
#     def __init__(self):
#         self.numbers_seen = []
#         self.sum_seen = set()
​
#     def add(self, number: int) -> None:
#         self.numbers_seen.append(number)
#         if (len(self.numbers_seen) == 1):
#             return
#         self.sum_seen.update({x + number for x in self.numbers_seen[:-1]})    
​
#     def find(self, value: int) -> bool:
#         return True if value in self.sum_seen else False
​
# Your TwoSum object will be instantiated and called as such:
