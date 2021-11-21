#soln - Leetcode Modulo + Array
class Bucket():
    def __init__(self):
        self.bucket = []
        
    def get(self, key):
        for (k,v) in self.bucket:
            if k == key:
                return v
        return -1
    
    def update(self, key, value):
        found = False
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] = (key, value)
                found = True
                break
        if not found:
            self.bucket.append((key, value))
    
    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]
​
class MyHashMap(object):
    def __init__(self):
        self.key_space = 4999 #arbitrarily large prime, in this case largest prime <5e3
        self.hash_table = [Bucket() for i in range(self.key_space)]
​
    def put(self, key, value):
        hash_key = key % self.key_space
