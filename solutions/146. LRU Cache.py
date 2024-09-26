# from collections import OrderedDict
# class LRUCache:
#     def __init__(self, capacity: int):
#         self.ordered_dict = OrderedDict()
#         self.capacity = capacity
        
#     def get(self, key: int) -> int:
#         if key in self.ordered_dict:
#             ans = self.ordered_dict[key] 
#             self.ordered_dict.move_to_end(key)
#         else: 
#             ans = -1
#         return ans
​
#     def put(self, key: int, value: int) -> None:
#         if key in self.ordered_dict:
#             self.ordered_dict[key] = value
#             self.ordered_dict.move_to_end(key)
#             return
        
#         if len(self.ordered_dict) >= self.capacity:
#             self.ordered_dict.popitem(last=False)
#         self.ordered_dict[key] = value
​
# double linked list solution
class ListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev=None
        self.next=None
​
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict: Dict[int, ListNode] = {} #key: key, value: node
        # head <> ... <> tail
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next, self.tail.prev = self.tail, self.head
​
    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            val = node.val
            self.remove(node)
            self.add_to_tail(node)
        else:
            val = -1
        return val
​
    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.remove(self.dict[key])
            new_node = ListNode(key,value)
            self.add_to_tail(new_node)
            self.dict[key] = new_node
            return
​
        if len(self.dict) >= self.capacity:
            node_to_remove = self.head.next
            self.remove(node_to_remove)
            del self.dict[node_to_remove.key]
            
        new_node = ListNode(key,value)
        self.add_to_tail(new_node)
        self.dict[key] = new_node
        
    def add_to_tail(self, node:ListNode) -> None:
        prev_end = self.tail.prev
        prev_end.next, node.prev = node, prev_end
        node.next, self.tail.prev = self.tail, node
    
    def remove(self, node) -> None:
        node.next.prev, node.prev.next = node.prev, node.next
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
​
