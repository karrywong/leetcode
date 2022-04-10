class Solution:
    def minOperations(self, logs: List[str]) -> int:
        #Straightforward, time O(N), space O(1)
        count = 0
        for log in logs:
            if log == "../":
                count -= 1 if count > 0 else 0
            elif log != "./":
                count += 1
        return count
