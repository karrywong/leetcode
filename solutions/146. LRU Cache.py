# double linked list solution
class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
​
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        node = self.dict[key]
        self.remove(node)
        self.add(node)
        return node.val
​
    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            old_node = self.dict[key] 
            self.remove(old_node)
            # add new node
            node = ListNode(key, value)
            self.dict[key] = node
            self.add(node)
            return
            
        # Check capacity before inserting node
        if len(self.dict) >= self.capacity:
            node_to_delete = self.head.next
            self.remove(node_to_delete)
            del self.dict[node_to_delete.key]
        # add new node
        node = ListNode(key, value)
        self.dict[key] = node
        self.add(node)
                
    def add(self, node) -> None:
        prev_end = self.tail.prev
        prev_end.next = node
        node.prev = prev_end
