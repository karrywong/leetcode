# #Approach 1 - link list, time O(N/K) w/ K = hash key, space O(K+M) w/ K = #predefined buckets and M = # unique values
# class Node:
#     def __init__(self, value, nextNode=None):
#         self.value = value
#         self.next = nextNode
        
# class Bucket(Node):
#     def __init__(self):
#         self.head = Node(0) # a pseudo head
        
#     def insert(self, newValue):
#         if not self.exists(newValue): # if not existed, add the new element to the head.
#             newNode = Node(newValue, self.head.next)
#             self.head.next = newNode # set the new head.
        
#     def delete(self, value):
#         prev = self.head
#         curr = self.head.next
#         while curr is not None:
#             if curr.value == value:
#                 # remove the current node
#                 prev.next = curr.next
#                 return
#             prev = curr
#             curr = curr.next  
            
#     def exists(self, value):
#         curr = self.head.next
#         while curr is not None:
#             if curr.value == value:
#                 # value existed already, do nothing
#                 return True
#             curr = curr.next
#         return False        


#Approach 2 - BST, time O(log(N/K)), space O(N+K)
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = None
        self.right = None

class BSTree:
    def __init__(self):
        self.root = None
    
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None or val == root.val:
            return root
        return self.searchBST(root.left, val) if val < root.val else self.searchBST(root.right, val)
    
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        elif val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        return root
        
    
    def successor(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.val
    
    def predecessor(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.val

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
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

    def remove(self, key: int) -> None:
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].delete(key)

    def contains(self, key: int) -> bool:
        bucketIndex = self._hash(key)
        return self.bucketArray[bucketIndex].exists(key)
    
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
