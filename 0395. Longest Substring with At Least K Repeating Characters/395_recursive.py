class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        counter = collections.Counter(s)
        c = counter.most_common()[-1][0]
        if counter[c] >= k:
            return len(s)

        return max([self.longestSubstring(ss, k) for ss in s.split(c)])
