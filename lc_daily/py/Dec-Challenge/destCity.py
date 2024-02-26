class Sol:
    def destCity(self, paths):
        pathMap = {}

        for i in paths:
            if not pathMap.get(i[0]):
                pathMap[i[0]] = i[1]
        sources = pathMap.keys()
        dest = pathMap.values()

        for i in dest:
            if i not in sources:
                return i


sln = Sol()
print(sln.destCity(
    [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]))
