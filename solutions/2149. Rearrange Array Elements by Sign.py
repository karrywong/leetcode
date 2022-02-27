class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        #Weekly contest
        neg_num, pos_num = [], []
        for num in nums:
            if num < 0:
                neg_num.append(num)
            else:
                pos_num.append(num)
        ans = []        
        for pos, neg in zip(pos_num, neg_num):
            ans += [pos, neg]
        return ans
