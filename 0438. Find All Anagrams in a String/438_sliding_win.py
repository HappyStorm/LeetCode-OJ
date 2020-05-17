class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        plen, pct = len(p), collections.Counter(p)
        sct = collections.Counter(s[:plen-1])
        for cid, c in enumerate(s[plen-1:], plen-1):
            sct[c] += 1
            if sct == pct:
                ans += [cid-plen+1]

            sct[s[cid-plen+1]] -= 1
            if sct[s[cid-plen+1]] == 0:
                del sct[s[cid-plen+1]]

        return ans
