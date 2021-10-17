class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        #got stuck and consulted discussions on DFS implementation
        #soln 1 by kejin
        #def dfs(s, res):
        #    if s <= n:
        #        res.append(s)
        #        t = s*10
        #        if t <= n:
        #            for i in range(10):
        #                dfs(t + i, res)
        #res = []
        #for k in range(1,10):
        #    dfs(k, res)
        #return res
    
        #soln 2, idea by SharpQuagga (miscellaneous)
        lst = [str(i) for i in range(1,n+1)]
        return sorted(lst)
        
​
