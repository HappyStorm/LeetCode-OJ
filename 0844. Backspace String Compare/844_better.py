class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i, j = len(S)-1, len(T)-1
        sct, tct = 0, 0
        while (i>=0) or (j>=0):
            while i>=0:
                if S[i] == '#':
                    sct += 1

                elif sct>0:
                    sct -= 1

                else:
                    break

                i -= 1

            while j>=0:
                if T[j] == '#':
                    tct += 1

                elif tct>0:
                    tct -= 1

                else:
                    break

                j -= 1

            if i>=0 and j>=0 and (S[i] != T[j]):
                return False

            if (i>=0) != (j>=0):
                return False

            i-=1
            j-=1

        return True
