class Solution:

    def basic_rabin_karp(self, s, m):
        if m == 0:
            return True, ""

        pattern_set = {}
        for i in range(len(s)-m+1):
            hp = hash(s[i:i+m])
            if hp in pattern_set:
                for j in pattern_set[hp]:
                    if s[i:i+m] == s[j:j+m]:
                        return True, s[j:j+m]

            else:
                pattern_set[hp] = [i]

        return False, ""

    def longestDupSubstring(self, S: str) -> str:
        ans, n, l, r = "", len(S), 0, len(S)
        while l <= r:
            m = (l+r) // 2
            find, pattern = self.basic_rabin_karp(S, m)

            if find:
                l = m + 1
                ans = pattern if m > len(ans) else ans

            else:
                r = m - 1

        return ans
