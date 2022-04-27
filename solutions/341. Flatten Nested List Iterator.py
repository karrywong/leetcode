        self.stack = [[nestedList,0]]
            
    def next(self) -> int:
        self.make_stack_top_an_integer()
        cur_lst = self.stack[-1][0]
        cur_index = self.stack[-1][1]
        self.stack[-1][1] += 1
        return cur_lst[cur_index].getInteger()
    
    def hasNext(self) -> bool:
        self.make_stack_top_an_integer()
        return len(self.stack) > 0
​
    def make_stack_top_an_integer(self):
        while self.stack:
            cur_lst = self.stack[-1][0]
            cur_index = self.stack[-1][1]
            
            if len(cur_lst) == cur_index:
                self.stack.pop()
                continue
            
            if cur_lst[cur_index].isInteger():
                break
                
            new_lst = cur_lst[cur_index].getList()
            self.stack[-1][1] += 1
            self.stack.append([new_lst,0])
    
# class NestedIterator: #Soln 1 - DFS iterative
#     def __init__(self, nestedList: [NestedInteger]):
#         self.stack = list(reversed(nestedList))
#         # print(self.stack)
#     def next(self) -> int:
#         self.make_stack_top_an_integer()
#         return self.stack.pop().getInteger()
    
#     def hasNext(self) -> bool:
#         self.make_stack_top_an_integer()
#         return len(self.stack) > 0
    
#     def make_stack_top_an_integer(self):
#         while self.stack and not self.stack[-1].isInteger():
#             self.stack.extend(reversed(self.stack.pop().getList()))
​
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
