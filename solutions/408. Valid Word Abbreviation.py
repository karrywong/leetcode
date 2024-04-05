class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # Cleaner impl by sgxu79, time O(len(abbr)), space O(1)
        w_ptr, num = 0, 0
        for char in abbr:
            if char.isalpha():
                w_ptr += num
                if w_ptr >= len(word) or char != word[w_ptr]:
                    return False
                w_ptr += 1
                num = 0
            elif num == 0 and char == "0":
                return False
            else:
                num = 10*num + int(char)
        return w_ptr+num == len(word)
