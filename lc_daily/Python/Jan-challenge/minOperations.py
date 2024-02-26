from collections import defaultdict

class Sol:
    def minOperations(self, nums):
        hashMap = defaultdict(int)
        originalMap = {}

        for i in nums:
            hashMap[i] += 1

        originalMap = hashMap.copy()
        res = 0
        prev = 0
        operationsCount = {}

        for i in hashMap.keys():
            while hashMap[i] >= 1:
                if hashMap[i] in operationsCount:
                    res += operationsCount[hashMap[i]]
                    hashMap[i] = 0
                elif hashMap[i] == 1:
                    return -1
                elif hashMap[i] % 3 == 0:
                    res += hashMap[i] // 3
                    hashMap[i] %= 3
                elif (hashMap[i] - 1) % 3 == 0 and hashMap[i] > 4:
                    count = ((hashMap[i] - 1) // 3) - 1
                    res += count
                    hashMap[i] -= count * 3
                elif 2 <= hashMap[i] <= 4:
                    if hashMap[i] % 2 == 0:
                        res += hashMap[i] // 2
                        hashMap[i] %= 2
                    else:
                        res += hashMap[i] // 3
                        hashMap[i] %= 3
                else:
                    res += hashMap[i] // 3
                    hashMap[i] %= 3
                    res += hashMap[i] // 2
                    hashMap[i] %= 2

            if hashMap[i] not in operationsCount:
                operationsCount[originalMap[i]] = res - prev
                prev = res

        return res


sln = Sol()
print(sln.minOperations([2,3,3,2,2,4,2,3,4]))