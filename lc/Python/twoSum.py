class Sol:
    def twoSumII(self, numbers, target):
        l = 0
        r = len(numbers)-1

        while l < r:
            summ = numbers[l]+numbers[r]

            if summ == target:
                return [l+1, r+1]

            elif summ < target:
                l += 1
            else:
                r -= 1


sln = Sol()
print(sln.twoSumII([0, 0, 3, 4], 0))
