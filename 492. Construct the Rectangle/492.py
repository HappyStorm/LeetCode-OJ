class Solution(object):

    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        for i in range(int(math.sqrt(area)), 0, -1):
            if not area % i:
                return [i, int(area / i)] if i > int(area / i) else [int(area / i), i]
