class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldiers = []
        for rid, row in enumerate(mat):
            soldiers.append((rid, sum(row)))
        return list(map(lambda x: x[0], sorted(soldiers, key=lambda x: x[1])))[:k]
