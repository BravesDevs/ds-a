class Sol:
    def largestGoodInteger(self, num):
        res = set()
        for i in range(1, len(num)-1):
            if num[i-1] == num[i] and num[i] == num[i+1]:
                res.add(num[i-1:i+2])
        return str(max(res, key=int)) if res else ''


sln = Sol()
print(sln.largestGoodInteger("222"))
