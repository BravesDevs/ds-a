from collections import Counter


class Solution:
    def relativeSortArray(self, arr1, arr2):
        freq = Counter(arr1)
        arr1.sort()
        res = []
        for i in arr2:
            res.extend([i]*freq[i])
        for i in arr1:
            if i not in arr2:
                res.append(i)
        return res


sln = Solution()
print(sln.relativeSortArray([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [
      2, 1, 4, 3, 9, 6]))
