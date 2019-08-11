class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        d = {}
        for wid, word in enumerate(A):
            for c in word:
                if d.get(c):
                    d[c][wid] += 1

                else:
                    d[c] = [0] * len(A)
                    d[c][wid] = 1

        ans = []
        for k, v in d.items():
            ans += [k] * min(v)

        return ans