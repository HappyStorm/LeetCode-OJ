class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sct, tct, slen, tlen = 0, 0, len(s), len(t)
        while sct < slen and tct < tlen:
            if s[sct] == t[tct]:
                sct += 1

            tct += 1

        return sct == slen
