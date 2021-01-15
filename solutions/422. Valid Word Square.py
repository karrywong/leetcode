class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        
        for i in range(0, len(words)):
            if i != 0 and len(words[i-1]) < len(words[i]): 
                return False
            
            if len(words[i]) < i + 1: 
                continue
            temp1 = words[i][i:]
            temp2 = "".join([words[j][i] for j in range(i, len(words)) if len(words[j]) >= i + 1 ])
            if temp1 != temp2:
                return False
        return True
                
            
