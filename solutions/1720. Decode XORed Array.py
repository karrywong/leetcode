class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        #The inverse function of XOR is XOR itself, i.e. (A^B)^B=A and (A^B)^A=B
        ans = [first]
        for n in encoded:
            ans.append(ans[-1]^n)
        return ans
