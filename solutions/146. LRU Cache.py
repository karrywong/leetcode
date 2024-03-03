from collections import OrderedDict
class LRUCache(object):
    def __init__(self, capacity: int):
        """
        :type capacity: int
        """
        self.upper_bound = capacity
        self.dict = OrderedDict() #{4:4, 3:3}
​
    def get(self, key: int) -> int:
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dict:
            return -1
        self.dict.move_to_end(key)
        return self.dict[key]
​
    def put(self, key: int, value: int) -> None:
        """
        :type key: int
        :type value: int
        :rtype: void
        """
# ### Chuanbin suggested
#         val = self.get(key)
#         if val == value:
#             return
#         if val != -1:
#             self.dict[key] = value
#             self.dict.move_to_end(key)
#             return
            
#         if len(self.dict) >= self.upper_bound:
#             self.dict.popitem(last=False)   
#         self.dict[key] = value
​
### Karry
        if key in self.dict:
            self.dict[key] = value #update
            self.dict.move_to_end(key)
            return
​
        if len(self.dict) >= self.upper_bound:
            self.dict.popitem(last=False)
        self.dict[key] = value
​
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
