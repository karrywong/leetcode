class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n+1):
            # if i % 3 == 0 and i % 5 == 0:
            #     ans.append("FizzBuzz")
            # elif i % 3 == 0:
            #     ans.append("Fizz")
            # elif i % 5 == 0:
            #     ans.append("Buzz")
            # else:
            #     ans.append(str(i))
            
            ###Checking fewer conditions
            temp = ""
            divisible_by_3 = i % 3 == 0 
            divisible_by_5 = i % 5 == 0 
            
            if divisible_by_3:
                temp += "Fizz"
            if divisible_by_5:
                temp += "Buzz"
            if not temp:
                temp += str(i)
            ans.append(temp)
        return ans
