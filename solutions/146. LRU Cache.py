from collections import OrderedDict
​
​
class LRUCache:
    def __init__(self, capacity: int):
        self.ordered_dict = OrderedDict()
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key in self.ordered_dict:
            ans = self.ordered_dict[key] 
            self.ordered_dict.move_to_end(key)
        else: 
            ans = -1
        return ans
​
    def put(self, key: int, value: int) -> None:
        if key in self.ordered_dict:
            self.ordered_dict[key] = value
            self.ordered_dict.move_to_end(key)
            return
        
        if len(self.ordered_dict) >= self.capacity:
            self.ordered_dict.popitem(last=False)
        self.ordered_dict[key] = value
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
​
