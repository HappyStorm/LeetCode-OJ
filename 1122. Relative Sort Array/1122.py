class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        for e in arr2:
            ans += [e] * arr1.count(e)

        uni = []
        for e in arr1:
            if e not in arr2:
                uni += [e]

        return ans + sorted(uni)
