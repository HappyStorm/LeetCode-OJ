class Solution:
    def sortString(self, s: str) -> str:
        ans, counter = [], collections.Counter(s)
        while len(ans) < len(s):
            for alphabets in string.ascii_lowercase, string.ascii_lowercase[::-1]:
                for c in alphabets:
                    if counter[c]:
                        ans.append(c)
                        counter[c] -= 1
        return ''.join(ans)
