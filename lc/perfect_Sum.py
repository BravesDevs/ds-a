input2 = [4,7,8,2,3]

def perfect_Sum(input2):

# check if the array is not empty and contains integer
    if len(input2) == 0:
        return 999
    for i in input2:
        if type(i) != int:
            return 999


    cnt = 0
    for i in range(len(input2)):
        for j in range(i+1,len(input2)):
            if input2[i]+input2[j] == 12:
                cnt+=1
    return cnt if cnt>0 else 999

print(perfect_Sum(input2))