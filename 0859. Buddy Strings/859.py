class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False

        dup = set()
        if A == B:
            for a in A:
                if a in dup:
                    return True

                dup.add(a)

            return False

        ilist = []
        for i in range(len(A)):
            if A[i] != B[i]:
                ilist += [i]

        if len(ilist) > 2:
            return False

        if A[ilist[0]] == B[ilist[1]] and A[ilist[1]] == B[ilist[0]]:
            return True

        return False
