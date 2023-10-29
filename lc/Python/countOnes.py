def countOnes(listOnes):
    p1 = 0
    count = 0
    maxOnes = []
    while p1 < len(listOnes):
        if listOnes[p1] == 1:
            count += 1
            p1 += 1
        else:
            count = 0
            p1 += 1
        maxOnes.append(count)
    return max(maxOnes)


print(countOnes([1, 1, 1, 0, 1, 1]))
