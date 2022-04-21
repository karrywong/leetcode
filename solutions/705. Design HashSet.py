            root.left = self.deleteNode(root.left, key)
        else:
            if not (root.left or root.right):
                root = None
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val) #recursively delete surccessor in the right subtree
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
        return root
        
class Bucket:
    def __init__(self):
        self.tree = BSTree()
    
    def insert(self, value):
        self.tree.root = self.tree.insertIntoBST(self.tree.root, value)
    
    def delete(self, value):
        self.tree.root = self.tree.deleteNode(self.tree.root, value)
        
    def exists(self, value):
        return (self.tree.searchBST(self.tree.root, value) is not None)
​
​
class MyHashSet(object):
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
    
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
