from collections import deque
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # Runtime O(N), space O(1)
        t, f = -1, -1
        deqt, deqf = deque(), deque()
        ans = 0
        
        for idx, char in enumerate(answerKey):
            if char == "T":
                deqt.append(idx)
                if len(deqt) > k:
                    t = deqt.popleft()
            else:
                deqf.append(idx)
                if len(deqf) > k:
                    f = deqf.popleft()
            ans = max(ans, idx - f, idx - t)
        return ans
    
    # answerKey = "TTFF", k = 2
    # (idx, ans): (0,1)->(1,2)->(2,3)->(3,4)
    
    # answerKey = "TFFT", k = 1
    # (idx, ans): (0,1)->(1,2)->(2,2)->(3,3)
    
    # answerKey = "TTFTTFTT", k = 1
    # (idx, ans): (0,1)->(1,2)->
        
