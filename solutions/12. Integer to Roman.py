class Solution:
    def intToRoman(self, num: int) -> str:
        #soln 2 - Jake's solution, hash wisely
        ans = ''
        num = str(num)
        l = len(num)
        table = {0:['I','V'],1:['X','L'],2:['C','D'],3:['M']}
        for i in range(0,l):
            place = l - i - 1
            cur_d = int(num[i])
            if cur_d < 4:
                ans += table[place][0]*cur_d
            elif cur_d == 4:
                ans += table[place][0] + table[place][1]
            elif cur_d < 9:
                ans += table[place][1] + table[place][0]*(cur_d-5)
            else:
                ans += table[place][0] + table[place+1][0]     
        return ans
        
        #soln 1 - brute force hashtable        
        #htb = {0:"", 1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX",
        #       10:"X",20:"XX",30:"XXX",40:"XL",50:"L",60:"LX",70:"LXX",80:"LXXX",90:"XC",
        #       100:"C",200:"CC",300:"CCC",400:"CD",500:"D",600:"DC",700:"DCC",800:"DCCC",900:"CM",
        #       1000:"M",2000:"MM",3000:"MMM"}
        #ans = ""
        #lst = list(str(num))
        #for i in range(0, len(lst)):
        #    ans += htb[int(lst[i]) * 10**(len(lst)-i-1)]
        #return ans
        
        
​
            
        
