def addNums(num):
    if num < 10:
        return num
    num = sum(list(map(int, str(num))))
    return addNums(num)


print(addNums(10))
