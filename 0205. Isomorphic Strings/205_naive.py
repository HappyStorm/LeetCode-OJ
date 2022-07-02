class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dst, dts = dict(), dict()
        for sc, tc in zip(s, t):
            if sc not in dst and tc not in dts:
                dst[sc], dts[tc] = tc, sc
            else:
                if dst.get(sc) != tc or dts.get(tc) != sc:
                    return False
        return True
