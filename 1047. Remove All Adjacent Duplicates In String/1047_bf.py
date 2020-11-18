class Solution:
    def removeDuplicates(self, S: str) -> str:
        if len(S) == 1:
            return S

        while True:
            done = True
            for i in range(1, len(S)):
                if S[i] == S[i-1]:
                    S = S[:i-1] + S[i+1:]
                    done = False
                    break

            if done:
                return S
