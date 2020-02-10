class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        k = math.ceil(len(B) /len (A))
        for i in range(2):
            if B in A * (k+i):
                return k+i

        return -1