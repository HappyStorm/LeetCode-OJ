class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        return sum([c[0] for c in costs]) + sum(sorted([c[1] - c[0] for c in costs])[:len(costs)//2])
