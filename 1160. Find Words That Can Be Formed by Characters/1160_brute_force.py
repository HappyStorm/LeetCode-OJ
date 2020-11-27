class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charpower = collections.Counter(chars)
        ans = 0
        for word in words:
            ct = collections.Counter(word)
            if ct - charpower:
                continue
            else:
                ans += len(word)
        return ans
