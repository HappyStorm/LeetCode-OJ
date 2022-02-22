class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        return sum([26**i*(ord(v)-ord('A')+1) for i, v in enumerate(columnTitle[::-1])])
