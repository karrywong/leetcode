class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        flowerbed = [0] + flowerbed + [0]
        i = 1
        while i < len(flowerbed)-1:
            if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
                count += 1
                i += 1
            i += 1
        return True if count >= n else False
        
