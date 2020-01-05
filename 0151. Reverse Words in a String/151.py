class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([w for w in s.strip().split(' ')[::-1] if len(w)])
