class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Time O(N), Space O(1)
        left, right = 0, len(numbers) - 1
        val = numbers[left] + numbers[right]
        while val != target:
            if val < target:
                left += 1
            else:
                right -= 1
            val = numbers[left] + numbers[right]
        return [left+1, right+1]
