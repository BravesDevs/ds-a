class Sol:
    def restoreString(self, s, indices):
        sList = list(s)
        res = ['']*len(s)
        for char, index in zip(sList, indices):
            res[index] = char

        return ''.join(res)


sln = Sol()
print(sln.restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]))
