reverseStackLi = []

def reverseStack(S):
    if isEmpty(S):
        return
    
    data = S.pop()

    reverseStack(S)

    insertAtBotton(S, data)


def isEmpty(S):
    return False if len(S)>0 else True


def insertAtBotton(S,data):
    tempLi=[]
    if isEmpty(S):
        S.append(data)
        return
    else:
        while not isEmpty(S):
            tempLi.append(S.pop())
        insertAtBotton(S,data)

        while not isEmpty(tempLi):
            S.append(tempLi.pop()) 



arr = [1,2,3,4]
reverseStack(arr)
print(arr)
