class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cur, _len = 0, len(flowerbed)
        while cur < _len:
            if flowerbed[cur] == 0\
                    and (cur == 0 or flowerbed[cur-1] == 0)\
                    and (cur == _len-1 or flowerbed[cur+1] == 0):
                flowerbed[cur] = 1
                cur, n = cur+1, n-1

            cur += 1

            if n <= 0:
                return True

        return False
