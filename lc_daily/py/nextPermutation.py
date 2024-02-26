import itertools


class Sol:
    def nextPermutation(self, nums):
        permutations = [list(x) for x in itertools.permutations(nums)]
        newLi = []
        permutations.sort()
        for i in permutations:
            if i not in newLi:
                newLi.append(i)
        permutated = newLi[(newLi.index(nums)+1) % len(newLi)]
        for index, element in enumerate(nums):
            nums[index] = permutated[index]
        return nums


sln = Sol()
print(sln.nextPermutation([2, 2, 7, 5, 4, 3, 2, 2, 1]))
