class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1 or not arr:
            return 0

        _len, reduced_len = len(arr), 0
        cur, prev = 0, None
        graph = {}
        while cur < _len:
            is_reduce = False
            while cur+1 < _len and arr[cur] == prev:
                cur += 1
                is_reduce = True

            if arr[cur] in graph:
                graph[arr[cur]].append(reduced_len)
            else:
                graph[arr[cur]] = [reduced_len]

            prev = arr[cur]
            arr[reduced_len] = arr[cur]
            reduced_len += 1

            if is_reduce:
                graph[arr[cur]].append(reduced_len)
                arr[reduced_len] = arr[cur]
                reduced_len += 1

            cur += 1

        arr = arr[:reduced_len]

        queue, visited = [(0, 0)], {0}
        while queue:
            search = []
            for i, d in queue:
                if i == reduced_len-1:
                    return d

                for j in graph[arr[i]][::-1]:
                    if j not in visited:
                        search.append((j, d+1))
                        visited.add(j)

                graph[arr[i]].clear()

                for j in [i-1, i+1]:
                    if j not in visited and 0 <= j < _len:
                        search.append((j, d+1))
                        visited.add(j)
            queue = search
        return -1
