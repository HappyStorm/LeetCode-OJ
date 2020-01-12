class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i, _len = 0, len(flowerbed)
        while i < _len:
            if not flowerbed[i]\
                and (not i or not flowerbed[i-1])\
                and (i == _len-1 or not flowerbed[i+1]):
                flowerbed[i] = 1
                i += 1
                n -= 1

            i += 1

            if n <= 0:
                return True

        return False
