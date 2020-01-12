class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i, _len = 0, len(flowerbed)
        while i < _len and n > 0:
            if i == 0:
                if not flowerbed[i]:
                    if i < _len-1:
                        if not flowerbed[i+1]:
                            n -= 1
                            flowerbed[i] = 1
                    else:
                        n -= 1
                        flowerbed[i] = 1
                        break

            elif 0 < i and i < _len-1:
                if not flowerbed[i] and not flowerbed[i-1] and not flowerbed[i+1]:
                    n -= 1
                    flowerbed[i] = 1

            else:
                if not flowerbed[i] and not flowerbed[i-1]:
                    n -= 1
                    flowerbed[i] = 1

            i += 1

        return False if n else True
