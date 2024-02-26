class Sol:
    def compareVersion(self, version1, version2):
        firstVersions = [int(x) for x in version1.split('.')]
        secondVersions = [int(x) for x in version2.split('.')]

        maxLen = max(len(firstVersions), len(secondVersions))
        firstVersions += [0] * (maxLen - len(firstVersions))
        secondVersions += [0] * (maxLen - len(secondVersions))

        for v1, v2 in zip(firstVersions, secondVersions):
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1

        return 0


sln = Sol()
print(sln.compareVersion("0.1", "1.21.2"))
