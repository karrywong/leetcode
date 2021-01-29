class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
#         ### Soln 0 - easy soln, sorting with O(Nlog(N))
#         lst1 = list(s)
#         lst2 = list(t)
        
#         lst1.sort()
#         lst2.sort()
#         return lst1 == lst2
​
        ### Soln 1 - collections.counter
        count1 = collections.Counter(s)
        count2 = collections.Counter(t)
        return count1 == count2
        
