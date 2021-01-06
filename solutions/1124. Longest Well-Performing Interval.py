class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        ### Soln - with the help of discussion by SSigurd and Zeyuuuuuuu        
        score = 0
        res = 0
        seen = {}
        for i,hour in enumerate(hours):
            score = score + 1 if hour > 8 else score - 1
            if score not in seen:
                seen[score] = i
            
            # if from day-0 to day-i we get a score above 0
            # hourse[:i+1] is the longest WPI
            if score > 0:
                res = i + 1
            
            # if the score <= 0, which means we need to remove some day at the beginning that get -1
            # so we find the farthest day that we get (score - 1)
            # so that we can get 1 score from day[score-1] to day-i
            # remember we start at 0 and we can only +1 or -1 every one day
            # so we must get score-2 after we get score-1 when score <= 0
            # so the day[score-1] is farther than day[score-2] from day-i which can make a longer interval
            elif score - 1 in seen:
                res = max(res,i - seen[score-1])
        return res
​
