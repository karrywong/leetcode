class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        #Leetcode - factorial number system, time O(N^2), space O(N)
        #Refer to https://en.wikipedia.org/wiki/Factorial_number_system
        factorials, nums = [1], ['1']
        for i in range(1, n):
            # generate factorial system bases 0!, 1!, ..., (n - 1)!                
            factorials.append(factorials[i - 1] * i)
            # generate nums 1, 2, ..., n
            nums.append(str(i + 1))
        
        k -= 1  # fit k in the interval 0 ... (n! - 1)
        output = [] # compute factorial representation of k
        for i in range(n-1, -1, -1):
            idx = k // factorials[i]
            k -= idx * factorials[i]
            
            output.append(nums[idx])
            del nums[idx]
        return ''.join(output)
