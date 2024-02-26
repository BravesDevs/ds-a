import numpy as np


class Sol:
    def checkArithmetic(self, nums):
        nums.sort()
        return len(set(np.diff(nums))) == 1

    def checkArithmeticSubarrays(self, nums, l, r):
        result = []
        for i in range(len(l)):
            left = l[i]
            right = r[i]+1
            result.append(self.checkArithmetic(nums[left:right]))
        return result


sln = Sol()

print(sln.checkArithmeticSubarrays(
    [-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10],  [0, 1, 6, 4, 8, 7], [4, 4, 9, 7, 9, 10]))
