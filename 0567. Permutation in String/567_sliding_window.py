class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        plen, pct = len(s1), collections.Counter(s1)
        sct = collections.Counter(s2[:plen-1])
        for cid, c in enumerate(s2[plen-1:], plen-1):
            sct[c] += 1
            if sct == pct:
                return True

            sct[s2[cid-plen+1]] -= 1

            if sct[s2[cid-plen+1]] == 0:
                del sct[s2[cid-plen+1]]

        return False