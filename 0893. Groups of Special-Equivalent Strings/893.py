class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        spe = set()
        for s in A:
            sort_odd = ''.join(sorted(s[0::2]))
            sort_even = ''.join(sorted(s[1::2]))
            sort_str = sort_odd + sort_even
            spe.add(sort_str)
        return len(spe)
