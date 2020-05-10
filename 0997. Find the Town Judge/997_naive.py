class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        d = {i: [0, []] for i in range(1, N+1)}
        for t in trust:
            d[t[1]][0] += 1
            d[t[0]][1] += [t[1]]

        for k, v in d.items():
            if v[0] == N-1 and not v[1]:
                return k

        return -1
