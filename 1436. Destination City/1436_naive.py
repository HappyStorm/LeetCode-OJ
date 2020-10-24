class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        graph, cities = collections.defaultdict(list), set()
        for source, target in paths:
            graph[source] += [target]
            cities.add(source)
            cities.add(target)
        for city in cities:
            if len(graph[city]) == 0:
                return city

        return None
