class Sol:
    def largestOddNumber(self, num):
        ptr = len(num)-1
        while ptr >= 0 and int(num[ptr]) % 2 == 0:
            ptr -= 1

        return num[:ptr+1]


sln = Sol()
print(sln.largestOddNumber("4206"))
