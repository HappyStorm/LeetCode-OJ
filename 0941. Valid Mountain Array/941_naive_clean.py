class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3 or arr[0] >= arr[1]:
            return False

        up = True
        for i in range(1, len(arr)-1):
            if up:
                if arr[i] > arr[i+1]:
                    up = False
                if arr[i] == arr[i+1]:
                    return False
            else:
                if arr[i] <= arr[i+1]:
                    return False

        return True and not up
