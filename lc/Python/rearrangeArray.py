class Sol:
    def rearrangeArray(self, nums):
        lessLi = [x for x in nums if x < 0]
        moreLi = [x for x in nums if x > 0]

        res = []
        for i in range(len(lessLi)):
            res.extend([moreLi[i], lessLi[i]])
        return res


sln = Sol()
print(sln.rearrangeArray([3, 1, -2, -5, 2, -4]))
