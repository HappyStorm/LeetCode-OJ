class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans, _len = 0, len(arr)
        for i in range(_len-2):
            for j in range(i+1, _len-1):
                ok_a = abs(arr[i] - arr[j]) <= a
                if ok_a:
                    for k in range(j+1, _len):
                        ok_b = abs(arr[j] - arr[k]) <= b
                        ok_c = abs(arr[i] - arr[k]) <= c
                        ans += 1 if ok_b and ok_c else 0
        return ans
