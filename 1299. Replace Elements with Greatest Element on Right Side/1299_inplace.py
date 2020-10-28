class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        tmp = _max = arr[-1]
        for i in range(1, len(arr)):
            tmp = _max
            _max = max(_max, arr[~i])
            arr[~i] = tmp

        arr[-1] = -1
        return arr
