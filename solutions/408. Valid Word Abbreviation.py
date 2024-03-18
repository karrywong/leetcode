class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # Cleaner impl by sgxu79, time O(len(abbr)), space O()
        w_ptr, num = 0, 0
        for char in abbr:
            if char.isalpha():
                w_ptr += num
                if w_ptr >= len(word) or char != word[w_ptr]:
                    return False
                num = 0
                w_ptr += 1
            elif num == 0 and char == "0":
                return False
            else:
                num = int(char) + 10*num
        return w_ptr + num == len(word) 
        
        # # 1st attempt, time O(len(word)), space O(1)
        # w_ptr, a_ptr = 0, 0
        # num = 0
        # while a_ptr < len(abbr) and w_ptr < len(word):
        #     char = abbr[a_ptr]
        #     if char.isalpha():
        #         w_ptr += num
        #         if w_ptr >= len(word) or char != word[w_ptr]:
        #             return False
        #         num = 0
        #         w_ptr += 1
        #     else:
        #         if num == 0 and char == "0":
        #             return False
        #         num *= 10
        #         num += int(abbr[a_ptr])
        #     a_ptr += 1
        # if a_ptr < len(abbr): return False
        # return len(word[w_ptr:]) == num
