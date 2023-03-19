class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        self.paths = defaultdict(list)
        cities = set()
        for path in paths:
            self.paths[path[0]].append(path[1])
            cities.add(path[1])
        for city in cities:
            if len(self.paths[city]) == 0:
                return city
        