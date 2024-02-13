class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        # time O(N*M), N = len(words), M = max([len(w) for w in words]), space O(1)
        def is_palindrome(word: str) -> bool:
            l, r = 0, len(word) - 1
            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        for w in words:
            if is_palindrome(w):
                return w
        return ""
