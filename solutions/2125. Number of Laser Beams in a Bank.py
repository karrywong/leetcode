class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        #Straightforward, time O(M*N), space O(1), with M = len(bank), N = len(bank[0])
        ans = 0
        val = sum(map(int, bank[0]))
        for row in bank[1:]:
            temp = sum(map(int, row))
            if temp > 0:
                ans += val*temp
                val = temp
        return ans
