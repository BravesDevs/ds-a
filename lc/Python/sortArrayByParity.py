import math


class Sol:
    def sortArrayByParity(self, nums):
        liEven = [x for x in nums if x % 2 == 0]
        liOdd = [x for x in nums if x % 2 != 0]

        liEven.extend(liOdd)

        return liEven


sln = Sol()
print(sln.sortArrayByParity([1, 0, 3]))
