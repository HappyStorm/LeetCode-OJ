class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        _min = _max = arr[0]
        for n in arr[1:]:
            _min = min(_min, n)
            _max = max(_max, n)

        if ((_max - _min) % (len(arr)-1)):
            return False

        d = (_max - _min) // (len(arr)-1)

        cur = 0
        while cur < len(arr):
            if arr[cur] == (_min + cur * d):
                cur += 1
            elif (arr[cur] - _min) % d:
                return False
            else:
                pos = (arr[cur] - _min) // d
                if arr[cur] == arr[pos]:
                    return False
                arr[cur], arr[pos] = arr[pos], arr[cur]
        return True
