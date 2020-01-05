class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xy, xz, yz, yz_dict = 0, 0, 0, {}

        for xid, yaxis in enumerate(grid):
            max_xz = 0

            for yid, zaxis in enumerate(yaxis):
                xy += 1 if zaxis > 0 else 0
                max_xz = max(max_xz, zaxis)

                if yz_dict.get(str(yid)):
                    yz_dict[str(yid)] = max(yz_dict[str(yid)], zaxis)

                else:
                    yz_dict[str(yid)] = zaxis

            xz += max_xz

        yz = sum([v for v in yz_dict.values()])

        return xy + xz + yz
