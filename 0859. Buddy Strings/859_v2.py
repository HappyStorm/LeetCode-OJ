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

        else:
            pairs = []
            for a, b in zip(A, B):
                if a != b:
                    pairs += [[a, b]]

            if len(pairs) > 2:
                return False

            return pairs[0] == pairs[1][::-1]
