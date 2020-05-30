class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return [x[1] for x in sorted([(sqrt(x**2 + y**2), [x, y]) for x, y in points], key=lambda x: x[0])[:K]]
