class Solution:
    def removeDuplicates(self, S: str) -> str:
        if len(S) == 1:
            return S

        stk = [S[0]]
        for c in S[1:]:
            if stk and c == stk[-1]:
                stk.pop()
            else:
                stk.append(c)
        return ''.join(stk)
