class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        for e in arr2:
            while e in arr1:
                ans += [e]
                arr1.remove(e)

        return ans + sorted(arr1)
