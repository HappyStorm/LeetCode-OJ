class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i, _len = 0, len(flowerbed)
        while i < _len and n > 0:
            if not flowerbed[i]:
                if i == 0 or not flowerbed[i-1]:
                    if i == _len-1 or not flowerbed[i+1]:
                        flowerbed[i] = 1
                        n-=1
                        i+=1
            i+=1

        return False if n else True
