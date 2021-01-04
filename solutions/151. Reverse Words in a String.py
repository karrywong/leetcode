class Solution:
    def reverseWords(self, s: str) -> str:
        # ans = s.split()
        # ans = ans[::-1]
        # return " ".join(i for i in ans)
    
        temp = ""
        temp_list = []
      
        for i in range(0, len(s)):
            if s[i] != " ":
                temp = temp + s[i]
                if i == len(s) - 1:
                    temp_list.append(temp)
            else:
                if temp != "":
                    temp_list.append(temp)
                    temp = ""
        
        return " ".join(temp_list[::-1])
