class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones = sorted(stones)
            print(stones)
            x, y = stones[-2:]
            stones = stones[:-2]
            if x != y:
                stones.append(y-x)

        return stones[0] if stones else 0