class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = list(map(int, str(n)))
        _len = len(s)
        for i in range(_len-1, 0, -1):
            if s[i-1] < s[i]:
                rmin, rid = 10, -1
                for j in range(_len-1, i-1, -1):
                    if s[j] > s[i-1] and s[j] < rmin:
                        rmin, rid = s[j], j

                s[i-1], s[rid] = s[rid], s[i-1]
                ans = int(''.join(str(c) for c in s[:i]+s[i:][::-1]))
                return ans if ans < 2 << 31-1 else -1
        return -1
