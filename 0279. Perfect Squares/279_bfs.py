class Solution:
    def numSquares(self, n: int) -> int:
        if n <= 3:
            return n

        ct, psns = 0, []
        while ct**2 <= n:
            psns += [ct**2]
            ct += 1

        ans = 0
        queue = {n}
        while queue:
            ans += 1
            tmp_queue = set()
            for cur in queue:
                for psn in psns:
                    if cur == psn:
                        return ans

                    if cur < psn:
                        break

                    tmp_queue.add(cur-psn)

            queue = tmp_queue

        return ans
