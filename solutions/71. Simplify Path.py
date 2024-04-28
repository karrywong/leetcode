class Solution:
    def simplifyPath(self, path: str) -> str:    
        # time O(N), space O(N)
        stack = []
        for ele in path.split("/"):
            if ele == "..":
                if stack:
                    stack.pop()          
            elif ele == "" or ele == ".":
                continue
            else:
                stack.append(ele)
                
            # #TODO: 
            # # not begin with digit
            # if ele[0].isdigit() or ele[0] == "_":
            #     continue
        
        return "/" + ("/").join(stack)
    
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
