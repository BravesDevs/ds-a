class Solution(object):
    def letterCombinations(self, digits):
        mapDictionary = {
            '1': [],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        if len(digits) == 0:
            return []

        if len(digits) == 1:
            return mapDictionary[digits]

        result = mapDictionary[digits[0]]

        for i in range(1, len(digits)):
            temp = []
            for j in range(len(result)):
                for k in range(len(mapDictionary[digits[i]])):
                    temp.append(result[j] + mapDictionary[digits[i]][k])
            result = temp

        return result


# Path: letterCombinations.py
sln = Solution()
print(sln.letterCombinations("23"))
