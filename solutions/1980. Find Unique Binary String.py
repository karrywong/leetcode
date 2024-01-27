class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # nums = ["01","10"] -> [1, 2] range : 0 - 3, 00
        # nums = ["00","01"] -> [0, 1], 10
        # nums = ["111","011","001"] -> [7,3,1], range: 0-7, 000
        
        # defintion: n = len(binary string) = len(nums)
        #Goedos
        
        #diagonal argument: nums = ["01","10"] ans = 11
        # ["00","01"] = 10
        # ["111","011","001"] = [000]
        return "".join(["1" if num[idx] == "0" else "0" for idx, num in enumerate(nums)])
        
