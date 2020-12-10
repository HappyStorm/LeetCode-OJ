class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        if arr[0] < arr[1]:
            _dir = 1
        else:
            return False
        pivot = False
        for i in range(1, len(arr)-1):
            if arr[i] == arr[i+1]:
                return False
            if arr[i] < arr[i+1] and _dir == -1:
                return False
            if arr[i] > arr[i+1] and not pivot and _dir == 1:
                pivot = True
                _dir = -1

        return True if pivot else False
