class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        #Too many Failed attempts, conceptually trivial but coding hard
        #soln 2, LeetCode's sliding window
        n, m = len(s), len(words)
        wordlen = len(words[0])
        totallen = wordlen * m
        word_count = collections.Counter(words)
        
        #left, right pointers
        def sliding_window(left):
            words_found = collections.defaultdict(int)
            words_used = 0
            excess_word = False
            
            # Do the same iteration pattern as the previous approach - iterate
            # word_length at a time, and at each iteration we focus on one word
            for right in range(left, n, wordlen):
                if right + wordlen > n:
                    break
                
                sub = s[right : right+wordlen]
                if sub not in word_count:
                    # Mismatched word - reset the window
                    words_found = collections.defaultdict(int)
                    words_used = 0
                    excess_word = False
                    left = right + wordlen # Retry at the next index
                else:
                    # If we reached max window size or have an excess word
                    while right - left == totallen or excess_word:
                        # Move the left bound over continously
                        leftmost_word = s[left : left + wordlen]
                        left += wordlen
                        words_found[leftmost_word] -= 1
                        
                        if words_found[leftmost_word] == word_count[leftmost_word]:
                            # This word was the excess word
                            excess_word = False
                        else:
                            # Otherwise we actually needed it
                            words_used -= 1
                            
                    # Keep track of how many times this word occurs in the window
                    words_found[sub] += 1
                    if words_found[sub] <= word_count[sub]:
                        words_used += 1
                    else:
                        # Found too many instances already
                        excess_word = True
                    
                    if words_used == m and not excess_word:
                        # Found a valid substring
                        answer.append(left)
                    
        answer = []
        for i in range(wordlen):
            sliding_window(i)
        return answer
    
