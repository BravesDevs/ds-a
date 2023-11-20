import copy


class Sol:
    def letterCasePermutation(self, s):

        res = []

        inputSt = s
        outputSt = ''

        def solve(inSt, outSt):
            if not inSt:
                res.append(outSt)
                return
            elif not inSt[0].isalpha():
                solve(inSt[1:], outSt+inSt[0])
            else:
                solve(inSt[1:], outSt+inSt[0].lower())
                solve(inSt[1:], outSt+inSt[0].upper())
        solve(inputSt, outputSt)
        return res


sln = Sol()
print(sln.letterCasePermutation("a1b2"))
