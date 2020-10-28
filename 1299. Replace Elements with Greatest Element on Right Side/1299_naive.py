class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans, m = [-1], arr[-1]
        for i in range(1, len(arr)):
            ans.append(m)
            m = max(m, arr[~i])
        return ans[::-1]
