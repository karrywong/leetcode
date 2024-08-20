class Solution:
    def simplifyPath(self, path: str) -> str:    
        # time O(N), path O(N)
        stack = []
        for word in path.split('/'):
            if word == "..":
                if len(stack) > 0:
                    stack.pop()
            elif word == "." or len(word) == 0:
                continue
            else:
                stack.append(word)
                
            # #TODO: 
            # # not begin with digit
            # if ele[0].isdigit() or ele[0] == "_":
            #     continue
            
        return "/" + "/".join(stack)
    
# Testing
# path = "/home/"
# path.split("/") = ["home"]
# stack = ["home"] -> "/home"
​
# path = "/../"
# path.split("/") = [".."]
# stack = [] -> "/"
​
#  path = "/home//foo/"
# path.split("/") = ["home", "", "foo"]
# stack = ["home", "foo"] -> "/home/foo"
​
# path = "/home karry/" -> "/home karry"
