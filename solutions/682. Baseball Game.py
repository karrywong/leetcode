class Solution:
    def calPoints(self, ops: List[str]) -> int:
        #Straightforward, time O(N), space O(N)
        #Can be reduced to space O(1) by keeping track of last two seen numbers
        scores = [int(ops[0])]
        for char in ops[1:]:
            if char == "+":
                scores.append(sum(scores[-2:]))
            elif char == "C":
                scores.pop()
            elif char == "D":
                scores.append(scores[-1]*2)
            else:
                scores.append(int(char))
        return sum(scores)
