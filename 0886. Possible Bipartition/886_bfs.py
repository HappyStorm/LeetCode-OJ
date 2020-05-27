class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(N+1)]
        for st, ed in dislikes:
            graph[st] += [ed]
            graph[ed] += [st]

        queue, color = [], [None for _ in range(N+1)]
        for i in range(1, N+1):
            if color[i] is None:
                color[i] = 1

            else:
                continue

            queue = [i] + queue
            while queue:
                cur = queue.pop()
                for ed in graph[cur]:
                    if color[ed] is None:
                        queue = [ed] + queue
                        color[ed] = 0 if color[cur] else 1

                    if color[cur] == color[ed]:
                        return False

        return True
