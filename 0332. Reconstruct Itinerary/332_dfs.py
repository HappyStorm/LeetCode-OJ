class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        itineary = collections.defaultdict(list)
        for start, end in tickets:
            if start not in itineary:
                itineary[start] = [end]

            else:
                itineary[start] += [end]

        for k in itineary.keys():
            itineary[k].sort(reverse=True)

        routes = []
        def dfs(start):
            while itineary[start]:
                dfs(itineary[start].pop())

            routes.append(start)

        dfs("JFK")
        return routes[::-1]
