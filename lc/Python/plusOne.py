class Sol:
    def plusOne(self, digits):
        right = len(digits)-1
        digits[right] = (digits[right]+1) % 10

        while right > 0 and digits[right] == 0:
            right -= 1
            digits[right] = (digits[right]+1) % 10

        if digits[0] == 0:
            digits.insert(0, 1)

        return digits


sln = Sol()
print(sln.plusOne([0]))
