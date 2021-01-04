class Solution:
    def reverseWords(self, s: str) -> str:
        # ans = s.split()
        # for i in range(0,len(ans)):
        #     ans[i] = ans[i][::-1]
        # return " ".join(ans)
        
##Soln 1
        temp = ""
        temp_list = ""
        
        for i in range(0, len(s)):
            if s[i] != " ":
                temp += s[i]
            else:
                temp_list += temp[::-1] + " "
                temp = ""
        temp_list += temp[::-1]
        return temp_list
