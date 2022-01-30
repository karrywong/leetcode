class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        #Inspired by FACEPLANT in discussion, time O(len(typed)), space O(1)
        name, typed = name + ".", typed + "."
        i = j = 0
        cur = name[i]
        while i < len(name) and j < len(typed):
            if name[i] == typed[j] == cur:
                i += 1
                j += 1
            elif name[i] != cur and typed[j] == cur:
                j += 1
            elif name[i] != cur and typed[j] != cur:
                cur = name[i]
            else:
                return False
        return True
        
        # #First attempt, time O(len(typed)), space O(1)
        # if name == typed:
        # return True
        # if len(typed) < len(name) or name[-1] != typed[-1]:
        #     return False
        # i,j = 0,0
        # while i < len(name) and j < len(typed):
        #     if name[i] == typed[j]:
        #         i += 1
        #         j += 1
        #     elif j > 0 and typed[j] == typed[j-1]:
        #         j += 1
        #     else: 
        #         return False
        # if i == len(name) and j < len(typed):
        #     while j < len(typed) and typed[j] == name[-1]:
        #         j += 1
        # return i == len(name) and j == len(typed)         
