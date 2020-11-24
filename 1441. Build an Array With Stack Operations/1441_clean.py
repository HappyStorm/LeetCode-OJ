class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans, n = [], target[-1]
        target = set(target)
        for i in range(1, n+1):
            ans.append("Push")
            if i not in target:
                ans.append("Pop")
        return ans
