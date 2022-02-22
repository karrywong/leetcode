class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # # soln 2 - optimized, time O(len(coins)*amount), space O(amount)
        # tb = [1] + [None] * amount
        # for i in range(len(coins)):
        #     c = coins[i]
        #     if i == 0:
        #         for val in range(1, amount+1):
        #             tb[val] = 1 if val % c == 0 else 0
        #     else:
        #         if c <= amount:                 
        #             tb[c] += 1
        #             for val in range(c+1, amount+1):
        #                 tb[val] += tb[val-c]
        # return tb[-1]   
    
        #soln 1 - first attempt, time O(len(coins)*amount), space O(len(coins)*amount)
        tb = [[1] + [0] * amount for _ in range(len(coins))]
        for i in range(len(coins)):
            c = coins[i]
            if i == 0:
                for val in range(1, amount+1):
                    tb[0][val] = 1 if val % c == 0 else 0
            else:
                for val in range(1, amount+1):
                    if val < c: 
                        tb[i][val] = tb[i-1][val]
                    elif val == c:
                        tb[i][val] = tb[i-1][val] + 1
                    else:
                        tb[i][val] = tb[i-1][val] + tb[i][val-c]
        return tb[-1][-1]   
