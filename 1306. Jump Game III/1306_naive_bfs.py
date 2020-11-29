class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n, queue = len(arr), [start]
        while queue:
            cur = queue.pop()

            if arr[cur] == -1:
                continue

            if arr[cur] == 0:
                return True

            lid, rid = cur - arr[cur], cur + arr[cur]
            if lid >= 0:
                queue = [lid] + queue

            if rid < n:
                queue = [rid] + queue

            arr[cur] = -1

        return False
