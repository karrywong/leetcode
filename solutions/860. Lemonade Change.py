class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cnt = [0,0,0]
        for bill in bills:
            if bill == 5:
                cnt[0] += 1
            elif bill == 10:
                if cnt[0] == 0:
                    return False
                cnt[0] -= 1
                cnt[1] += 1
            else:
                if cnt[0] > 0 and cnt[1] > 0:
                    cnt[0] -= 1
                    cnt[1] -= 1
                    continue
                elif cnt[0] >= 3:
                    cnt[0] -= 3
                    continue
                else:
                    return False
        return True
