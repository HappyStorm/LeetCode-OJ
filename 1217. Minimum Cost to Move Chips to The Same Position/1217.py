class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd = even = 0
        for c in position:
            if c % 2:
                odd += 1
            else:
                even += 1
        return min(odd, even)
