class Solution:
    def reverse(self, x: int) -> int:
        ans = -int(str(x)[::-1][:-1]) if x < 0 else int(str(x)[::-1])
        return 0 if ans > 2147483647 or ans < -2147483648 else ans
