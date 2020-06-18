class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0

        n, l, r = len(citations), 0, len(citations)-1
        while l<=r:
            mid = (l+r) // 2

            if n-mid <= citations[mid]:
                 r = mid-1

            else:
                l = mid+1

        return n-l
