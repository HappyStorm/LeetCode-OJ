class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n, queue = len(arr), [start]
        while queue:
            cur = queue.pop()
            if arr[cur] == 0:
                return True

            for i in [cur - arr[cur], cur + arr[cur]]:
                if 0 <= i < n and arr[i] >= 0:
                    queue = [i] + queue

            arr[cur] = -arr[cur]

        return False
