class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        target = set(target)
        for i in range(1, n+1):
            if target:
                if i in target:
                    ans.append("Push")
                    target.remove(i)
                else:
                    ans.append("Push")
                    ans.append("Pop")
            else:
                return ans
        return ans
