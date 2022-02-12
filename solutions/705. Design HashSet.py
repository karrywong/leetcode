class MyHashSet:
    #LeetCode soln, use LinkedList as Bucket, hash function & collision handling
    #time O(N/K), space O(# buckets + # unique values inserted)
    def __init__(self):
        self.keyRange = 769
        self.bucketArray = [Bucket() for i in range(self.keyRange)]
        
    def _hash(self, key):
        return key % self.keyRange
    
    def add(self, key: int) -> None:
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].insert(key)
​
    def remove(self, key: int) -> None:
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].delete(key)
​
    def contains(self, key: int) -> bool:
        bucketIndex = self._hash(key)
        return self.bucketArray[bucketIndex].exists(key)
    
class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode
        
class Bucket:
    def __init__(self):
        self.head = Node(0) # a pseudo head
        
    def insert(self, newValue):
        if not self.exists(newValue): # if not existed, add the new element to the head.
            newNode = Node(newValue, self.head.next)
            self.head.next = newNode # set the new head.
        
    def delete(self, value):
        prev = self.head
        curr = self.head.next
        while curr is not None:
            if curr.value == value:
                # remove the current node
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next  
            
    def exists(self, value):
        curr = self.head.next
        while curr is not None:
            if curr.value == value:
                # value existed already, do nothing
                return True
            curr = curr.next
        return False        
    
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)