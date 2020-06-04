class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        _len = len(s)
        for i in range(_len//2):
            s[i], s[_len-i-1] = s[_len-i-1], s[i]
