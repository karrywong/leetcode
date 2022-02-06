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
    
#         #soln 1, LeetCode using Counter, can still be optimized using sliding window
#         #Time O((n-m*wordlen)*(m*wordlen)), space O(m+wordlen)
#         n, m = len(s), len(words)
#         wordlen = len(words[0])
#         totallen = wordlen * m
#         lookup = collections.Counter(words)
        
#         def check(i):
#             counts = lookup.copy()
#             word_used = 0
            
#             for j in range(i, i+totallen, wordlen):
#                 sub = s[j:j+wordlen]
#                 if counts[sub] > 0:
#                     counts[sub] -= 1
#                     word_used += 1
#                 else:
#                     break
#             return word_used == m
        
#         ans = []
#         for i in range(n-totallen+1):
#             if check(i):
#                 ans.append(i)
#         return ans
