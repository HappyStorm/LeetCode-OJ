class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph, visit = [[] for _ in range(numCourses)], [0 for _ in range(numCourses)]
        for ed, st in prerequisites:
            graph[st] += [ed]
            visit[ed] += 1

        queue = [i for i in range(numCourses) if visit[i] == 0][::-1]
        for i in range(numCourses):
            if not queue:
                return False

            cur = queue.pop()
            visit[cur] = 0

            for j in range(len(graph[cur])):
                visit[graph[cur][j]] -= 1
                if visit[graph[cur][j]] == 0:
                    queue = [graph[cur][j]] + queue

        return True
