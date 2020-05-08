class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        dx = coordinates[1][0] - coordinates[0][0]
        dy = coordinates[1][1] - coordinates[0][1]
        x, y = coordinates[0]
        for tx, ty in coordinates[2:]:
            if ((tx-x) * dy) - ((ty-y) * dx) != 0:
                return False

        return True
