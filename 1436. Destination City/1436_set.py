class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        src, tar = map(set, zip(*paths))
        return (tar - src).pop()
