# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next
​
class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        ans = PolyNode()
        ptr, ptr1, ptr2 = ans, poly1, poly2
        
        while ptr1 and ptr2:
            if ptr1.power > ptr2.power:
                # ptr.next = PolyNode(ptr1.coefficient, ptr1.power)
                # ptr = ptr.next
                ptr.next = ptr = ptr1
                ptr1 = ptr1.next
            elif ptr1.power < ptr2.power:
                # ptr.next = PolyNode(ptr2.coefficient, ptr2.power)
                # ptr = ptr.next
                ptr.next = ptr = ptr2
                ptr2 = ptr2.next
            else:
                x = ptr1.coefficient + ptr2.coefficient
                if x != 0:
                    ptr.next = ptr = PolyNode(x, ptr1.power)    
                    # ptr.next = PolyNode(x, ptr1.power)    
                    # ptr = ptr.next
                ptr1, ptr2 = ptr1.next, ptr2.next
        
        ptr.next = ptr1 if ptr1 else ptr2       
        return ans.next
