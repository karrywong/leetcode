# Class for a singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
​
class MyLinkedList:
    def __init__(self):
        # self.lst = [] //list attempt 
        self.size = 0
        self.head = ListNode(0) # sentinel node as pseudo-head
​
    def get(self, index: int) -> int:
        # return -1 if index >= len(self.lst) else self.lst[index] //list attempt 
        if index >= self.size: return -1
        curr = self.head
        for _ in range(index+1):
            curr = curr.next
        return curr.val
        
    def addAtHead(self, val: int) -> None:
        # self.lst = [val] + self.lst //list attempt 
        self.addAtIndex(0, val)
​
    def addAtTail(self, val: int) -> None:
        # self.lst.append(val) //list attempt 
        self.addAtIndex(self.size, val)
        
    def addAtIndex(self, index: int, val: int) -> None:
        # if index <= len(self.lst): //list attempt 
        #     self.lst.insert(index, val)
        
        if index <= self.size:
            self.size += 1
            pred = self.head
            for _ in range(index):
                pred = pred.next
            
            to_add = ListNode(val, pred.next)
            pred.next = to_add
​
    def deleteAtIndex(self, index: int) -> None:
        # if index < len(self.lst): //list attempt 
