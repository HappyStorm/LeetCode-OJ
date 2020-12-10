class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i, j, _len = 0, len(arr)-1, len(arr)
        while i < _len-1 and arr[i] < arr[i+1]:
            i += 1
        while j > 0 and arr[j] < arr[j-1]:
            j -= 1
        return 0 < i == j < _len-1
